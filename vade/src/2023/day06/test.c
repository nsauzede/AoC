/* SPDX-License-Identifier: GPL-3.0-or-later */

#define TEST_DONT_HIDE_MAIN_
#include "test.h"
#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <stdlib.h>
#ifdef _WIN32
#include <windows.h>
#else
#include <sys/time.h>
#endif

#define BOLDWHITE() "\x1b[0;1m"
#define RED() "\x1b[31m"
#define GREEN() "\x1b[32m"
#define BOLDGREEN() "\x1b[32;1m"
#define NRM() "\x1b[0m"

typedef struct test_ctx_s {
    int verbose;
    int fail_this;
    int curr;
} test_ctx_t;

typedef struct test_state_s {
    int fail_not_success;
    int line;
    const char *str;
    int v1, v2;
} test_state_t;

typedef struct test_s {
    test_ctx_t *ctx;
    test_node_t *node;
    test_state_t state;
} test_t;

static int success_(test_state_t *state, int line, const char *str) {
    state->fail_not_success = 0;
    state->line = line;
    state->str = str;
    return 1;
}

static int fail_(test_state_t *state, int line, const char *str) {
    state->fail_not_success = 1;
    state->line = line;
    state->str = str;
    return 0;
}

int assert_true_(test_t *test, int line, int v, const char *str) {
    test_ctx_t *ctx = test->ctx;
    test_state_t *state = &test->state;
    //printf("%s: line=%d\n", __func__, line);
    //printf("Testing if assert %d must fail.. (fail_this=%d)\n", curr, fail_this);
    if ((ctx->curr + 1) == ctx->fail_this) {    // curr is 0-based and fail_this is 1-based
        printf("Making this assert %d fail\n", ctx->curr);
        return fail_(state, line, str);
    }
    ctx->curr++;
    if (v) {
        //printf("Assert success line=%d\n", line);
        return success_(state, line, str);
    }
    //printf("Assert failure line=%d\n", line);
    return fail_(state, line, str);
}

int assert_or_(struct test_s *test, int line, assert_result_t res) {
    test_ctx_t *ctx = test->ctx;
    test_state_t *state = &test->state;
    //printf("%s: line=%d\n", __func__, line);
    //printf("Testing if assert %d must fail.. (fail_this=%d)\n", curr, fail_this);
    if ((ctx->curr + 1) == ctx->fail_this) {    // curr is 0-based and fail_this is 1-based
        printf("Making this assert %d fail\n", ctx->curr);
        return fail_(state, line, "fail_this");
    }
    ctx->curr++;
    if (res.v) {
        //printf("Assert success line=%d\n", line);
        return success_(state, line, "success");
    }
    //printf("Assert failure line=%d\n", line);
    return fail_(state, line, "fail");
}

static void print_failure_(test_state_t *state) {
    assert(state->fail_not_success);
    printf(">\t%s\n", state->str);
    //printf("E\tAssertionError: %d != %d\n", state->v1, state->v2);
    printf("E\tAssertionError: False is not True\n");
    //printf("FAILED %s:%d:%s::%s - AssertionError: %s\n", node->file, node->state.line, node->package, node->name, node->state.str);
}

static unsigned getclock_ms() {
#ifdef WIN32
    return GetTickCount();
#else
    struct timeval tv;
    gettimeofday(&tv, 0);
    return tv.tv_sec*1000.0 + tv.tv_usec/1000.0;
#endif
}

static int run_tests_(test_ctx_t *ctx, test_t *tests, int n_tests) {
    // TODO: maybe implement fail-fast/not.. based on ctx ?
    unsigned clock_ms0 = getclock_ms();
    printf("%s==================================================================== test session starts =====================================================================\n", BOLDWHITE());
    printf("collected %d items%s\n\n", n_tests, NRM());
    int failed = 0;
    int passed = 0;
    float elapsed_sec = 0.10;
    for (int i = 0; i < n_tests; i++) {
        //printf("%s: Running test node %d.. failed=%d node=%p\n", __func__, i, failed, node);
        test_t *test = &tests[i];
        test_node_t *node = test->node;
        test->ctx = ctx;
        node->fptr(test);
        const char *status = "PASSED";
        const char *pre = GREEN();
        const char *post = NRM();
        if (test->state.fail_not_success) {
            status = "FAILED";
            pre = RED();
            failed++;
        } else {
            passed++;
        }
        printf("%s::%s::%s %s%s%s\n", node->file, node->package, node->name, pre, status, post);
    }
    unsigned clock_ms1 = getclock_ms();
    elapsed_sec = (clock_ms1 - clock_ms0) / 1000.0;
    //printf("%s: failed=%d\n", __func__, failed);
    if (failed > 0) {
        printf("\n========================================================================== FAILURES ==========================================================================\n");
        for (int i = 0; i < n_tests; i++) {
            test_t *test = &tests[i];
            test_node_t *node = test->node;
            //printf("%s: Evaluating test node %d for failure.. node=%p\n", __func__, i, node);
            if (test->state.fail_not_success) {
                printf("___________________________________________________________________ %s.%s ___________________________________________________________________\n", node->package, node->name);
                printf("\n%s:%d: AssertionError\n", node->file, test->state.line);
                print_failure_(&test->state);
                //printf("================================================================== short test summary info ===================================================================\n");
                //printf("FAILED %s:%d:%s::%s - AssertionError: %s\n", node->file, test->state.line, node->package, node->name, test->state.str);
            }
        }
        printf("\n================================================================ %d failed, %d passed in %.02fs ================================================================\n", failed, passed, elapsed_sec);
    } else {
        const char *pre1 = GREEN();
        const char *pre2 = BOLDGREEN();
        const char *post = NRM();
        printf("\n%s================================================================ %s%d passed%s%s in %.02fs ================================================================%s\n", pre1, pre2, passed, post, pre1, elapsed_sec, post);
    }
    return failed > 0;
}

// Note: ctx is not cleared on entry
static void parse_args_(test_ctx_t *ctx, int argc, const char *argv[]) {
    int arg = 1;
    while (arg < argc) {
        if (!strcmp(argv[arg], "-f")) {
            if (++arg < argc) {
                ctx->fail_this = atoi(argv[arg]);
                //printf("Will make test %d to fail\n", ctx->fail_this);
            } else {
                printf("Argument missing\n");
                exit(1);
            }
        } else if (!strcmp(argv[arg], "-v")) {
            ctx->verbose++;
        }
        arg++;
    }
}

void add_node_(test_node_t **nodes, test_node_t *node) {
    node->next = *nodes;
    *nodes = node;
}

static int scan_tests_(test_t **tests, int *n_tests, /*test_ctx_t *ctx,*/ test_node_t *nodes) {
    //ctx = ctx; // TODO: maybe implement sorting, filtering.. based on ctx ?
    int n_nodes = 0;
    test_node_t *node = nodes;
    int i = 0;
    while (node) {
        //printf("%s: Scanning test node %d node=%p\n", __func__, i, node);
        if (!node->fptr) {
            printf("Nil fptr 1");
            break;
        }
        n_nodes++;
        node = node->next;
        i++;
    }
    *n_tests = n_nodes;
    *tests = (test_t *)calloc(*n_tests, sizeof(test_t));
    node = nodes;
    i = 0;
    while (node) {
        if (!node->fptr) {
            printf("Nil fptr 2");
            break;
        }
        (*tests)[i].node = node;
        node = node->next;
        i++;
    }
    return 0;
}

#ifdef ENABLE_TEST_TESTS
#if 0
static g_count = 0;
static void test0(test_state_t *state) {
    ASSERT_TRUE(0 == g_count);
    g_count += 5;
}
static void test1(test_state_t *state) {
    ASSERT_TRUE(5 == g_count);
    g_count *= 2;
}
static test_node_t test_011_nodes[] = {
    {0, "this_file", "foo_package1", "foo_name1", test0},
    {0, "this_file", "foo_package2", "foo_name2", (void (*)(test_t*))2345},
};
TEST(TestTest, test_021_run_tests, {
    
})
#endif
TEST(TestTest, test_031_scan_tests) {
    test_node_t nodes[] = {
        {0, "foo_file1", "foo_package1", "foo_name1", (void (*)(test_t*))1234},
        {0, "foo_file2", "foo_package2", "foo_name2", (void (*)(test_t*))2345},
    };
    nodes[0].next = &nodes[1];
    int n_nodes = sizeof(nodes) / sizeof(nodes[0]);
    int n_tests = 0;
    test_t *tests = 0;
    scan_tests_(&tests, &n_tests, /*test_ctx_t *ctx,*/ nodes);
    ASSERT_TRUE(n_nodes == n_tests);
    for (int i = 0; i < n_tests; i++) {
        test_node_t *node = tests[i].node;
        ASSERT_TRUE(nodes[i].file == node->file);
        ASSERT_TRUE(nodes[i].package == node->package);
        ASSERT_TRUE(nodes[i].name == node->name);
        ASSERT_TRUE(nodes[i].fptr == node->fptr);
    }
    free(tests);
}
TEST(TestTest, test_021_add_node) {
    test_node_t nodes[] = {
        {0, "foo_file1", "foo_package1", "foo_name1", (void (*)(test_t*))1234},
        {0, "foo_file2", "foo_package2", "foo_name2", (void (*)(test_t*))2345},
    };
    int n_nodes = sizeof(nodes) / sizeof(nodes[0]);
    test_node_t *l_nodes = 0;
    for (int i = 0; i < n_nodes; i++) {
        add_node_(&l_nodes, &nodes[i]);
    }
    int found_nodes = 0;
    test_node_t *node = l_nodes;
    int j = 0;
    while (node) {
        int i = n_nodes - j - 1;
        //printf("i=%d j=%d\n", i, j);
        ASSERT_TRUE(nodes[i].file == node->file);
        ASSERT_TRUE(nodes[i].package == node->package);
        ASSERT_TRUE(nodes[i].name == node->name);
        ASSERT_TRUE(nodes[i].fptr == node->fptr);
        node = node->next;
        j++;
        found_nodes++;
    }
    ASSERT_TRUE(n_nodes == found_nodes);
}
TEST(TestTest, test_011_parse_args_and_fail_this) {
    test_ctx_t ctx = { .verbose = 0, .fail_this = 42, .curr = 0 };
    parse_args_(&ctx, 0, 0);
    ASSERT_TRUE(42 == ctx.fail_this);
    char const *argv[] = {"dummy", "-f", "0"};
    parse_args_(&ctx, 3, argv);
    ASSERT_TRUE(0 == ctx.fail_this);
}
TEST(TestTest, test_012_parse_args_and_verbose) {
    test_ctx_t ctx = { .verbose = -2, .fail_this = 0, .curr = 0};
    parse_args_(&ctx, 0, 0);
    ASSERT_TRUE(-2 == ctx.verbose);
    char const *argv[] = {"dummy", "-v"};
    parse_args_(&ctx, 2, argv);
    ASSERT_TRUE(-1 == ctx.verbose);
    parse_args_(&ctx, 2, argv);
    ASSERT_TRUE(0 == ctx.verbose);
}
TEST(TestTest, test_013_parse_args_and_fail_this_and_verbose) {
    test_ctx_t ctx = { .verbose = 0, .fail_this = 666, .curr = 0 };
    ctx.verbose = -2;
    char const *argv1[] = {"dummy"};
    parse_args_(&ctx, 1, argv1);
    ASSERT_TRUE(-2 == ctx.verbose);
    ASSERT_TRUE(666 == ctx.fail_this);
    char const *argv2[] = {"dummy", "-v", "-f", "0", "-v"};
    parse_args_(&ctx, 5, argv2);
    ASSERT_TRUE(0 == ctx.verbose);
    ASSERT_TRUE(0 == ctx.fail_this);
}
const int this_very_line = __LINE__;
TEST(TestTest, test_001_ensure_assert_true_sets_correct_line) {
    ASSERT_TRUE(42 == 42);
    assert((this_very_line + 2) == TEST_OPAQUE_POINTER_->state.line);
    ASSERT_TRUE(666 == 666);
    assert((this_very_line + 4) == TEST_OPAQUE_POINTER_->state.line);
}
#if 0
// does it make sense for a test to not test anything anyway ?
TEST(TestTest, test_000_ensure_empty_test_is_valid) {
}
#endif
#endif

test_node_t *nodes_;
int main(int argc, char *argv[]) {
    test_ctx_t ctx = { .verbose = 0, .fail_this = 0, .curr = 0 };
    parse_args_(&ctx, argc, (const char **)argv);
    test_t *tests = 0;
    int n_tests = 0;
    scan_tests_(&tests, &n_tests, /*&ctx,*/ nodes_);
    int res = run_tests_(&ctx, tests, n_tests);
    free(tests);
    return res;
}
