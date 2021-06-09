
function myFunc(arg) {
	console.log(`arg was => ${arg}`);
}

setTimeout(myFunc, 1500, 'funky');

const timeoutObj = setTimeout(() => {
  console.log('timeout beyond time');
}, 1500);

const immediateObj = setImmediate(() => {
  console.log('immediately executing immediate');
});

const intervalObj = setInterval(() => {
  console.log('interviewing the interval');		//每x毫秒执行一次
}, 500);


//清除定时器：
//clearTimeout(timeoutObj);
//learImmediate(immediateObj);
//clearInterval(intervalObj);
