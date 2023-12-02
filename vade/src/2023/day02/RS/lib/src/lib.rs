#[cfg(test)]
mod tests {
    fn parse(games: Vec<&str>) -> Vec<Vec<(u32, u32, u32)>> {
        let mut res = Vec::new();
        for (_i, s) in games.iter().enumerate() {
            let v1: Vec<&str> = s.split(':').collect();
            let v2: Vec<&str> = v1[0].split(' ').collect();
            let _game = v2[1].parse::<u32>().unwrap();
            let v3: Vec<&str> = v1[1].split(';').collect();
            let mut res0 = Vec::new();
            for (_j, rgb) in v3.iter().enumerate() {
                let v4: Vec<&str> = rgb.split(',').collect();
                let mut rgb0: (u32, u32, u32) = (0, 0, 0);
                for comp in v4 {
                    let v5: Vec<&str> = comp.split(' ').collect();
                    let q = v5[1].parse::<u32>().unwrap();
                    let col = v5[2];
                    match col {
                        "red" => rgb0.0 = q,
                        "green" => rgb0.1 = q,
                        "blue" => rgb0.2 = q,
                        _ => {}
                    }
                }
                res0.push(rgb0);
            }
            res.push(res0);
        }
        res
    }
    fn compute(part: u8, rgb: (u32, u32, u32), input: Vec<Vec<(u32, u32, u32)>>) -> u32 {
        let mut res = 0;
        for (i, vec) in input.iter().enumerate() {
            if part == 0 {
                let mut possible = true;
                for &(r, g, b) in vec {
                    if r > rgb.0 || g > rgb.1 || b > rgb.2 {
                        possible = false;
                        break;
                    }
                }
                if possible {
                    res += i as u32 + 1
                }
            } else {
                let mut rgb0: (u32, u32, u32) = (0, 0, 0);
                for &(r, g, b) in vec {
                    if r > rgb0.0 {
                        rgb0.0 = r
                    }
                    if g > rgb0.1 {
                        rgb0.1 = g
                    }
                    if b > rgb0.2 {
                        rgb0.2 = b
                    }
                }
                let res0 = rgb0.0 * rgb0.1 * rgb0.2;
                res += res0;
            }
        }
        res
    }
    const INP01: &str = r#"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"#;
    const RES01: u32 = 8;
    const INP1: &str = "../../input1";
    const RES1: u32 = 3035;
    const RES02: u32 = 2286;
    const RES2: u32 = 66027;
    #[test]
    fn part2_parse002() {
        let result = compute(1, (12, 13, 14), parse(INP01.lines().collect()));
        assert_eq!(RES02, result);
    }
    #[test]
    fn part2_parse003() {
        use std::fs;
        let string = &fs::read_to_string(INP1).unwrap();
        let result = compute(1, (12, 13, 14), parse(string.lines().collect()));
        assert_eq!(RES2, result);
    }
    #[test]
    fn part1_parse000() {
        let result = parse(vec![
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        ]);
        assert_eq!(vec![vec![(4, 0, 3), (1, 2, 6), (0, 2, 0)]], result);
    }
    #[test]
    fn part1_parse001() {
        let result = parse(INP01.lines().collect());
        assert_eq!(
            vec![
                vec![(4, 0, 3), (1, 2, 6), (0, 2, 0)],
                vec![(0, 2, 1), (1, 3, 4), (0, 1, 1)],
                vec![(20, 8, 6), (4, 13, 5), (1, 5, 0)],
                vec![(3, 1, 6), (6, 3, 0), (14, 3, 15)],
                vec![(6, 3, 1), (1, 2, 2)],
            ],
            result
        );
    }
    #[test]
    fn part1_parse002() {
        let result = compute(0, (12, 13, 14), parse(INP01.lines().collect()));
        assert_eq!(RES01, result);
    }
    #[test]
    fn part1_parse003() {
        use std::fs;
        let string = &fs::read_to_string(INP1).unwrap();
        let result = compute(0, (12, 13, 14), parse(string.lines().collect()));
        assert_eq!(RES1, result);
    }
    #[test]
    fn part1_000() {
        let result = compute(0, (12, 13, 14), vec![vec![(4, 0, 3), (1, 2, 6), (0, 2, 0)]]);
        assert_eq!(1, result);
    }
    #[test]
    fn part1_001() {
        let result = compute(
            0,
            (12, 13, 14),
            vec![
                vec![(4, 0, 3), (1, 2, 6), (0, 2, 0)],
                vec![(0, 2, 1), (1, 3, 4), (0, 1, 1)],
            ],
        );
        assert_eq!(3, result);
    }
    #[test]
    fn part1_002() {
        let result = compute(
            0,
            (12, 13, 14),
            vec![
                vec![(4, 0, 3), (1, 2, 6), (0, 2, 0)],
                vec![(0, 2, 1), (1, 3, 4), (0, 1, 1)],
                vec![(20, 8, 6), (4, 13, 5), (1, 5, 0)],
            ],
        );
        assert_eq!(3, result);
    }
    #[test]
    fn part1_003() {
        let result = compute(
            0,
            (12, 13, 14),
            vec![
                vec![(4, 0, 3), (1, 2, 6), (0, 2, 0)],
                vec![(0, 2, 1), (1, 3, 4), (0, 1, 1)],
                vec![(20, 8, 6), (4, 13, 5), (1, 5, 0)],
                vec![(3, 1, 6), (6, 3, 0), (14, 3, 15)],
                vec![(6, 3, 1), (1, 2, 2)],
            ],
        );
        assert_eq!(8, result);
    }
}
