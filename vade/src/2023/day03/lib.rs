#[cfg(test)]
mod tests {
    #[derive(Copy, Clone)]
    struct Number {
        num: u32,
        start: u32,
        end: u32,
        y: u32,
    }
    #[derive(Debug, Copy, Clone)]
    struct Sym {
        sym: char,
        x: u32,
        y: u32,
    }
    fn parse(part: u8, inp: Vec<&str>) -> u32 {
        let mut syms: Vec<Sym> = Vec::new();
        let mut nums: Vec<Number> = Vec::new();
        for (j, s) in inp.iter().enumerate() {
            let mut num = Number {
                num: 0,
                start: 0,
                end: 0,
                y: 0,
            };
            let mut num0 = String::from("");
            for (i, c) in s.char_indices() {
                if c.is_digit(10) {
                    if num0.is_empty() {
                        num.start = i as u32;
                        num.y = j as u32;
                    }
                    num0.push(c);
                    // special case when a number ends with the line
                    if i == s.len() - 1 {
                        num.end = i as u32;
                        num.num = num0.parse::<u32>().unwrap();
                        nums.push(num);
                    }
                } else {
                    if !num0.is_empty() {
                        num.end = i as u32 - 1;
                        num.num = num0.parse::<u32>().unwrap();
                        nums.push(num);
                        num0.clear();
                    }
                    if c != '.' {
                        syms.push(Sym {
                            sym: c,
                            x: i as u32,
                            y: j as u32,
                        });
                    }
                }
            }
        }
        let mut res = 0;
        if part == 0 {
            for num in nums {
                for sym in &syms {
                    if is_neib(num, *sym) {
                        res += num.num;
                    }
                }
            }
        } else {
            for sym in &syms {
                if sym.sym != '*' {
                    continue;
                }
                let mut count = 0;
                let mut n1 = 0;
                let mut n2 = 0;
                for num in &nums {
                    if is_neib(*num, *sym) {
                        if count == 0 {
                            n1 = num.num;
                        }
                        if count == 1 {
                            n2 = num.num;
                        }
                        count += 1;
                    }
                }
                if count == 2 {
                    res += n1 * n2;
                }
            }
        }
        res
    }
    fn is_neib(num: Number, sym: Sym) -> bool {
        let y = if num.y > 0 { num.y - 1 } else { 0 };
        let start = if num.start > 0 { num.start - 1 } else { 0 };
        sym.y >= y && sym.y <= num.y + 1 && sym.x >= start && sym.x <= num.end + 1
    }
    #[test]
    fn part1_is_neib0() {
        let result = is_neib(
            Number {
                num: 0,
                start: 0,
                end: 2,
                y: 0,
            },
            Sym {
                sym: '?',
                x: 3,
                y: 1,
            },
        );
        assert_eq!(true, result);
    }
    #[test]
    fn part1_is_neib1() {
        let result = is_neib(
            Number {
                num: 0,
                start: 5,
                end: 7,
                y: 0,
            },
            Sym {
                sym: '?',
                x: 3,
                y: 1,
            },
        );
        assert_eq!(false, result);
    }
    const INP01: &str = r#"467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."#;
    const RES01: u32 = 4361;
    const INP101: &str = r#"...939...784.
.....*.......
167....+.+873
.....513....."#;
    const RES101: u32 = 2325;
    const INP1: &str = "input1";
    //const RES1: u32 = 538237;//too low (missed numbers ending with the line)
    const RES1: u32 = 539637;
    const RES02: u32 = 467835;
    const RES2: u32 = 82818007;
    #[test]
    fn part2_inp01() {
        let result = parse(1, INP01.lines().collect());
        assert_eq!(RES02, result);
    }
    #[test]
    fn part2_inp1() {
        use std::fs;
        let string = &fs::read_to_string(INP1).unwrap();
        let result = parse(1, string.lines().collect());
        assert_eq!(RES2, result);
    }
    #[test]
    fn part1_inp01() {
        let result = parse(0, INP01.lines().collect());
        assert_eq!(RES01, result);
    }
    #[test]
    fn part1_inp101() {
        let result = parse(0, INP101.lines().collect());
        assert_eq!(RES101, result);
    }
    #[test]
    fn part1_inp1() {
        use std::fs;
        let string = &fs::read_to_string(INP1).unwrap();
        let result = parse(0, string.lines().collect());
        assert_eq!(RES1, result);
    }
    #[test]
    fn part1_parse1() {
        let result = parse(0, vec!["467..114..", "...*......"]);
        assert_eq!(467, result);
    }
    #[test]
    fn part1_parse0() {
        let result = parse(0, vec!["467..114.."]);
        assert_eq!(0, result);
    }
}
