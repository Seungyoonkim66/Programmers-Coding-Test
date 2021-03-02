var progresses = [95, 90, 99, 99, 80, 99];
var speeds = [1, 1, 1, 1, 1, 1]
let answer = [0];
// days는 각 프로그래스마다 소요되는 일수를 저장 
let days = progresses.map((progress, index) => Math.ceil((100 - progress) / speeds[index]));

let maxDay = days[0];

// i는 days의 인덱스 
// j는 answer의 인덱스 
for (let i = 0, j = 0; i < days.length; i++) {
    if (days[i] <= maxDay) {
        answer[j] += 1;
    } else {
        maxDay = days[i];
        answer[++j] = 1;
    }
}



