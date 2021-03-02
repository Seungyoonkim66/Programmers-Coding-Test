// using Queue

var priorities = [1,1,9,1,1,1]
var location = 0

var answer = 0;
print_order =[];
for (let i=0; i<priorities.length; i++){
    let obj = {};
    obj[i] = priorities[i];
    print_order.push(obj);
}
// console.log(print_order);
// [
//     { '0': 1 },
//     { '1': 1 },
//     { '2': 9 },
//     { '3': 1 },
//     { '4': 1 },
//     { '5': 1 }
//   ]

for (let i=0; i<priorities.length; i++){
    for (let j=i+1;j<priorities.length;j++){
        if (priorities[j] > priorities[i] && priorities){
            print_order.shift();
            let obj = {};
            obj[i] = priorities[i];
            print_order.push(obj);
            break;
        }
        else if (j == priorities.length){
            print_order.shift();
        }
    }
}
// console.log(print_order.filter(p => { p[String(location)] != undefined}));
print_order.forEach((loc, i) => {
    if (loc[String(location)] != undefined) {
        answer = i+1;
    }
});
// console.log(print_order);


console.log(answer); // 5
