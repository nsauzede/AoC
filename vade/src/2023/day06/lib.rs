#[cfg(test)]
mod tests {
    fn compute(inp: Vec<(u64, u64)>) -> u64 {
        let mut res = 1;
        for (tt, drec) in inp {
            let mut th1 = 0;
            while th1 < tt {
                if th1 * (tt - th1) > drec {
                    break;
                }
                th1 += 1;
            }
            let mut th2 = tt - 1;
            while th2 != 0 {
                if th2 * (tt - th2) > drec {
                    break;
                }
                th2 -= 1;
            }
            if th2 > th1 {
                res *= th2 - th1 + 1
            }
        }
        res
    }
    const INP02: [(u64, u64); 1] = [(71530, 940200)];
    const RES02: u64 = 71503;
    #[test]
    fn part2_inp02() {
        let result = compute(Vec::from(INP02));
        assert_eq!(RES02, result);
    }
    const INP2: [(u64, u64); 1] = [(41777096, 249136211271011)];
    const RES2: u64 = 27363861;
    #[test]
    fn part2_inp2() {
        let result = compute(Vec::from(INP2));
        assert_eq!(RES2, result);
    }
    const INP01: [(u64, u64); 3] = [(7, 9), (15, 40), (30, 200)];
    const RES01: u64 = 288;
    #[test]
    fn part1_inp01() {
        let result = compute(Vec::from(INP01));
        assert_eq!(RES01, result);
    }
    const INP1: [(u64, u64); 4] = [(41, 249), (77, 1362), (70, 1127), (96, 1011)];
    const RES1: u64 = 771628;
    #[test]
    fn part1_inp1() {
        let result = compute(Vec::from(INP1));
        assert_eq!(RES1, result);
    }
}
