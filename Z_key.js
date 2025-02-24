// 定义按键事件
function triggerKeyPress(keyCode) {
    const event = new KeyboardEvent('keydown', {
        key: 'z',
        code: 'KeyZ',
        keyCode: keyCode,
        which: keyCode,
        bubbles: true
    });
    document.dispatchEvent(event);
}

// 随机间隔时间函数
function getRandomInterval(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// 开始自动按键
let intervalId = setInterval(() => {
    triggerKeyPress(90); // 90 是 Z 键的 keyCode
}, getRandomInterval(300, 500));

// 提示用户如何停止
console.log("按下 Ctrl+C 或在控制台中运行 clearInterval(intervalId) 来停止自动按键。");