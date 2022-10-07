var switch_on = new Audio('audio/on.wav');
var switch_off = new Audio('audio/off.wav');
var light = ['off', 'on', 'off', 'off', 'off', 'on', 'on', 'off', 'off', 'on', 'off', 'off', 'on', 'on', 'off', 'off', 'off', 'on', 'off', 'off', 'off', 'off', 'off', 'on', 'off', 'on', 'off', 'off', 'off', 'on', 'on', 'on', 'off', 'off', 'on', 'off', 'on', 'on', 'off', 'on', 'off', 'on', 'on', 'off', 'off', 'off', 'on', 'off', 'off', 'off', 'on', 'on', 'off', 'off', 'off', 'on', 'off', 'on', 'on', 'off', 'on', 'on', 'on', 'off', 'off', 'off', 'on', 'on', 'off', 'on', 'off', 'off', 'off', 'on', 'on', 'on', 'off', 'off', 'on', 'off', 'off', 'on', 'on', 'on', 'on', 'off', 'off', 'on', 'off', 'on', 'off', 'on', 'on', 'on', 'on', 'on', 'off', 'on', 'on', 'off', 'off', 'on', 'off', 'off', 'off', 'off', 'on', 'on', 'off', 'on', 'off', 'off', 'off', 'on', 'on', 'off', 'on', 'on', 'on', 'off', 'off', 'on', 'on', 'off', 'off', 'off', 'on', 'on', 'off', 'off', 'on', 'on', 'off', 'off', 'on', 'on', 'off', 'on', 'off', 'on', 'on', 'on', 'on', 'on', 'off', 'on', 'on', 'off', 'off', 'on', 'on', 'off', 'off', 'off', 'on', 'on', 'off', 'on', 'off', 'on', 'off', 'on', 'on', 'off', 'off', 'on', 'on', 'off', 'off', 'on', 'on', 'off', 'off', 'on', 'on', 'off', 'off', 'on', 'on', 'off', 'off', 'on', 'off', 'off', 'off', 'on', 'on', 'off', 'off', 'off', 'on', 'on', 'off', 'off', 'on', 'on', 'on', 'off', 'off', 'off', 'off', 'off', 'on', 'on', 'off', 'on', 'on', 'on', 'off', 'on', 'on', 'off', 'off', 'off', 'off', 'on', 'off', 'on', 'on', 'off', 'off', 'on', 'off', 'on'];
(async function() {
  for (var i = 0; i < light.length; i++){
    document.getElementById('lamp').src = './img/' + light[i] + '.png';
    if (i > 0 && light[i-1] != light[i]) {
      if (light[i] == "on") switch_on.play(); else switch_off.play();
    }
    await new Promise(r => setTimeout(r, 1000));
  }
})();
