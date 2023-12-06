/* SPDX-License-Identifier: GPL-3.0-or-later */

#ifndef TEST_H__
#define TEST_H__

/* Test API */

#define TEST(package, name) TEST_(package, name)
#define ASSERT_TRUE(v) ASSERT_TRUE_(v)
#define ASSERT_OR(r) ASSERT_OR_(r)
#define ASSERT_EQU(v1, v2) ASSERT_EQU_(v1, v2)

/* Test Internals (subject to change) */

#if defined(__TINYC__) && !defined(_WIN32)
/* <Sigh..> https://lists.nongnu.org/archive/html/tinycc-devel/2022-10/msg00016.html */
#include <sys/cdefs.h>
#undef __attribute__
#endif

#ifdef __cplusplus
extern "C" {
#endif

struct test_s;
extern int assert_true_(struct test_s *test, int line, int v, const char *s);
#define TEST_OPAQUE_POINTER_ test_opaque_pointer_
#define ASSERT_TRUE_(v) do{if(!assert_true_(TEST_OPAQUE_POINTER_, __LINE__, v, #v))return;}while(0)
#define ASSERT_EQU_(v1, v2) do{long _v1=v1,_v2=v2,_v=_v1==_v2;static char buf[300]; \
    if(!_v){sprintf(buf,"%lu != %lu\n",v1,v2);} \
    if(!assert_true_(TEST_OPAQUE_POINTER_, __LINE__, _v, buf))return;}while(0)

typedef struct {
    int v;
    char *s;
} assert_result_t;
extern int assert_or_(struct test_s *test, int line, assert_result_t res);
#define ASSERT_OR_(res) do{if(!assert_or_(TEST_OPAQUE_POINTER_, __LINE__, res))return;}while(0)

typedef struct test_node_s {
    struct test_node_s *next;
    const char *file;
    const char *package;
    const char *name;
    void (*fptr)(struct test_s *TEST_OPAQUE_POINTER_);
} test_node_t;
extern test_node_t *nodes_;
extern void add_node_(test_node_t **nodes, test_node_t *node);

#define NAME_(package, name) test_ ## package ## _ ## name
#define NODE_(package, name) test_ ## package ## _ ## name ## _node
#define CTOR_(package, name) test_ ## package ## _ ## name ## _ctor

#define TEST_(package, name) \
static void NAME_(package, name)(struct test_s *TEST_OPAQUE_POINTER_); \
static test_node_t NODE_(package, name) = {0, __FILE__, #package, #name, NAME_(package, name)}; \
static void __attribute__ ((constructor)) CTOR_(package, name)(void) { add_node_(&nodes_, &NODE_(package, name)); } \
static void NAME_(package, name)(struct test_s *TEST_OPAQUE_POINTER_)
#ifndef TEST_DONT_HIDE_MAIN_
#define main(...) hide_standard_main__(__VA_ARGS__)
#endif

#ifdef __cplusplus
}
#endif

#endif
