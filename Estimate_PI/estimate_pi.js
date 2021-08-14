// estimate_pi function
const estimate_pi = (n) => {
    num_point_circle = 0;
    num_point_total = 0;
    for (let i = 0; i < n; i++) {
        let x = Math.random();
        let y = Math.random();
        let distance = Math.pow(x, 2) + Math.pow(y, 2);
        if (distance <= 1) num_point_circle++;
        num_point_total++;
    }
    return 4 * num_point_circle / num_point_total;
}

// test cases
const test_cases = [1, 10, 100, 1000, 10000, 100000, 1000000];
for (var test_case of test_cases) console.log(estimate_pi(test_case));

// example output
/**

4
3.2
3.24
3.16
3.1384
3.13868
3.139648

*/