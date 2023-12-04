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
            use std::collections::HashMap;
            struct Card {
                copies: u32,
                wins: Vec<u32>,
            }
            let mut cards: HashMap<u32, Card> = HashMap::new();
            for (j, s) in inp.iter().enumerate() {
                use regex::Regex;
                let space_pattern = Regex::new(r"\s+").unwrap();
                let s0 = space_pattern.replace_all(s, " ");
                let v1: Vec<&str> = s0.split(':').collect();
                let v2: Vec<&str> = v1[0].split(' ').collect();
                let card = v2[1].parse::<u32>().unwrap();
                println!("card={}..", card);
                /*
                                let entry = cards.entry(card).or_insert(Card {
                                    copies: 0,
                                    wins: vec![],
                                });
                                println!("card={} before n={}", card, entry.copies);
                                entry.copies += 1;
                                println!("card={} after n={}", card, entry.copies);
                */
                let mut have = Vec::new();
                let v3: Vec<&str> = v1[1].split('|').collect();
                let v4: Vec<&str> = v3[0].split(' ').collect();
                let mut wins = Vec::new();
                for num in v4 {
                    if num == "" {
                        continue;
                    }
                    let num = num.parse::<u32>().unwrap();
                    wins.push(num);
                }
                let v4: Vec<&str> = v3[1].split(' ').collect();
                for num in v4 {
                    if num == "" {
                        continue;
                    }
                    let num = num.parse::<u32>().unwrap();
                    have.push(num);
                }
                let mut points = 0;
                for num in have {
                    if wins.contains(&num) {
                        println!("winning {}", num);
                        points += 1;
                    }
                }
                let mut copies = Vec::new();
                for j in card + 1..card + 1 + points {
                    let copy = cards.entry(j).or_insert(Card {
                        copies: 0,
                        wins: vec![],
                    });
                    copy.copies += 1;
                    println!("copying card {} => n={}", j, copy.copies);
                    copies.push(j);
                }
                let entry = cards.entry(card).or_insert(Card {
                    copies: 0,
                    wins: vec![],
                });
                println!("card={} before n={}", card, entry.copies);
                entry.copies += 1;
                println!("card={} after n={}", card, entry.copies);
                for copy in copies {
                    entry.wins.push(copy);
                }
                //*entry+=points;
            }
            let mut cards2: HashMap<u32, u32> = HashMap::new();
            let mut sorted_cards: Vec<_> = cards.keys().collect();
            sorted_cards.sort();
            for id in sorted_cards {
                let card = cards.get(id).unwrap();
                println!("card={} copies={} wins={:?}", id, card.copies, card.wins);
                let n = card.wins.len() as u32;
                for copy in &card.wins {
                    let card2 = cards2.entry(*copy).or_insert(0);
                    *card2 += n;
                }
                //res += card.copies
                //res += card.wins.len() as u32
            }
            for (id, count) in cards2 {
                println!("id{} count={}", id, count);
            }
            /*                        if part==1 {
                                        res += 1; // count the current one
                                        let v4: Vec<&str> = v3[1].split(' ').collect();
                                        let mut nwins = 0;
                                        for (_j, val0) in v4.iter().enumerate() {
                                            if *val0 == "" {continue;}
                                            let val = val0.parse::<u32>().unwrap();
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
    */
}
