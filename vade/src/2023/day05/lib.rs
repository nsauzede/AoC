#[cfg(test)]
mod tests {
    fn parse(part: u8, inp: Vec<&str>) -> u32 {
        let mut res = 0;
        if part == 0 {
            for (_j, s) in inp.iter().enumerate() {
            }
        } else {
        }
        res
    }
    const INP01: &str = r#"seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"#;
    const RES01: u32 = 35;
    #[test]
    fn part1_inp01() {
        let result = parse(0, INP01.lines().collect());
        assert_eq!(RES01, result);
    }
/* //
    const INP1: &str = "input1";
    const RES1: u32 = 21485;
    #[test]
    fn part1_inp1() {
        use std::fs;
        let string = &fs::read_to_string(INP1).unwrap();
        let result = parse(0, string.lines().collect());
        assert_eq!(RES1, result);
    }
    const RES02: u32 = 30 + 0 * 1000;
    #[test]
    fn part2_inp01() {
        let result = parse(1, INP01.lines().collect());
        assert_eq!(RES02, result);
    }
    //const RES2: u32 = 2010; // too low
    const RES2: u32 = 11024379; // good
    #[test]
    fn part2_inp1() {
        use std::fs;
        let string = &fs::read_to_string(INP1).unwrap();
        let result = parse(1, string.lines().collect());
        assert_eq!(RES2, result);
    }
// */
}
