#[cfg(test)]
mod tests {
    fn compute(part: u8, input: &str) -> u32 {
        let mut res = 0;
        for text in input.lines() {
            let mut first = 0;
            let mut second = 0;
            let mut word = String::from("");
            for c in text.chars() {
                if let Some(digit) = c.to_digit(10) {
                    word.clear();
                    if first==0 {
                        first = digit
                    } else {
                        second = digit
                    }
                } else if part==1 {
                    word.push(c);
                    let words = vec!["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
                    for (i, _) in word.char_indices() {
                        if let Some(index) = words.iter().position(|&x| x == &word[i..]) {
                            if first==0 {
                                first = index as u32 + 1
                            } else {
                                second = index as u32 + 1
                            }
                            word.clear();
                            word.push(c);
                            break
                        }
                    }
                }
            }
            if second == 0 {
                second = first;
            }
            res += first * 10 + second
        }
        res
    }
    #[test]
    fn digit_11() {
        let result = compute(0, "1");
        assert_eq!(11, result);
    }
    #[test]
    fn digit_23() {
        let result = compute(0, "23");
        assert_eq!(23, result);
    }
    #[test]
    fn digit_34() {
        let result = compute(0, "z3x4t");
        assert_eq!(34, result);
    }
    const INP01:&str = r#"1abc2
        pqr3stu8vwx
        a1b2c3d4e5f
        treb7uchet"#;
    const RES01:u32 = 142;
    const INP1:&str = "../../input1";
    const RES1:u32 = 55816;
    #[test]
    fn digit_inp01() {
        let result = compute(0, INP01);
        assert_eq!(RES01, result);
    }
    #[test]
    fn digit_inp1() {
        use std::fs;
        let result = compute(0, &fs::read_to_string(INP1).unwrap());
        assert_eq!(RES1, result);
    }
    #[test]
    fn part2_11() {
        let result = compute(1, "onezxt");
        assert_eq!(11, result);
    }
    #[test]
    fn part2_23() {
        let result = compute(1, "gtkjtwo1gfnk6one7zxthreeljdst");
        assert_eq!(23, result);
    }
    const INP02:&str = r#"two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen"#;
    const RES02:u32 = 281;
    const INP2:&str = "../../input1";
    const RES2:u32 = 54980;
    #[test]
    fn part2_inp01() {
        let result = compute(1, INP02);
        assert_eq!(RES02, result);
    }
    #[test]
    fn part2_inp1() {
        use std::fs;
        let result = compute(1, &fs::read_to_string(INP2).unwrap());
        assert_eq!(RES2, result);
    }
}
