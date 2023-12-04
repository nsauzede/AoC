#[cfg(test)]
mod tests {
    fn parse(part: u8, inp: Vec<&str>) -> u32 {
        let mut res = 0;
        if part == 0 {
            for (j, s) in inp.iter().enumerate() {
                use regex::Regex;
                let space_pattern = Regex::new(r"\s+").unwrap();
                let s0 = space_pattern.replace_all(s, " ");
                let v1: Vec<&str> = s0.split(':').collect();
                let v2: Vec<&str> = v1[0].split(' ').collect();
                let card = v2[1].parse::<u32>().unwrap();
                println!("card={}", card);
                let mut wins = Vec::new();
                let mut have = Vec::new();
                let v3: Vec<&str> = v1[1].split('|').collect();
                let v4: Vec<&str> = v3[0].split(' ').collect();
                for num in v4 {
                    wins.push(num);
                }
                let v4: Vec<&str> = v3[1].split(' ').collect();
                for num in v4 {
                    have.push(num);
                }
                let mut points = 0;
                for num in have {
                    if num == "" {
                        continue;
                    }
                    if wins.contains(&num) {
                        println!("winning {}", num);
                        if points == 0 {
                            points = 1
                        } else {
                            points *= 2
                        }
                    }
                }
                println!("points={}", points);
                res += points;
            }
        } else {
            for (j, s) in inp.iter().enumerate() {
                use regex::Regex;
                let space_pattern = Regex::new(r"\s+").unwrap();
                let s0 = space_pattern.replace_all(s, " ");
                let v1: Vec<&str> = s0.split(':').collect();
                let v2: Vec<&str> = v1[0].split(' ').collect();
                let card = v2[1].parse::<u32>().unwrap();
                println!("card={}", card);
                let mut wins = Vec::new();
                let mut have = Vec::new();
                let v3: Vec<&str> = v1[1].split('|').collect();
                let v4: Vec<&str> = v3[0].split(' ').collect();
                for num in v4 {
                    wins.push(num);
                }
                let v4: Vec<&str> = v3[1].split(' ').collect();
                for num in v4 {
                    have.push(num);
                }
                let mut points = 0;
                for num in have {
                    if num == "" {
                        continue;
                    }
                    if wins.contains(&num) {
                        println!("winning {}", num);
                        if points == 0 {
                            points = 1
                        } else {
                            points *= 2
                        }
                    }
                }
                println!("points={}", points);
                res += points;
            }
            /*
                        if part==1 {
                            use std::collections::HashMap;
                            let mut cards:HashMap<u32,u32> = HashMap::new();
                            res += 1; // count the current one
                            let v4: Vec<&str> = v3[1].split(' ').collect();
                            let mut nwins = 0;
                            for (_j, val0) in v4.iter().enumerate() {
                                if *val0 == "" {
                                    //println!("skipping");
                                    continue;
                                }
                                let val = val0.parse::<u32>().unwrap();
                                //println!("win={}", val);
                                have.push(val);
                                if wins.contains(&val) {
                                    println!("winning {}", val);
                                    nwins+=1;
                                }
                            }
                            for j in card+1..card+1+nwins {
                                dict[j]=1;
                            }
                        }
            */
        }
        res
    }
    const INP01: &str = r#"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"#;
    const RES01: u32 = 13;
    #[test]
    fn part1_inp01() {
        let result = parse(0, INP01.lines().collect());
        assert_eq!(RES01, result);
    }
    const INP1: &str = "input1";
    const RES1: u32 = 21485;
    #[test]
    fn part1_inp1() {
        use std::fs;
        let string = &fs::read_to_string(INP1).unwrap();
        let result = parse(0, string.lines().collect());
        assert_eq!(RES1, result);
    }
    /*
    const RES02: u32 = 30;
    #[test]
    fn part2_inp01() {
        let result = parse(1, INP01.lines().collect());
        assert_eq!(RES02, result);
    }
        const RES2: u32 = 82818007;
        #[test]
        fn part2_inp1() {
            use std::fs;
            let string = &fs::read_to_string(INP1).unwrap();
            let result = parse(1, string.lines().collect());
            assert_eq!(RES2, result);
        }
    */
}
