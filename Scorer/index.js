let fileSelect = document.getElementById('file-select');
let fileVideo = document.getElementById('file-video');
let audioFrequency = document.getElementById('audio-frequency');
let audioFrequencyList = document.getElementById('audio-frequency-list');

let A4 = 440;
let A4_INDEX = 57;
let STEP = Math.pow(2, 1 / 12);
let notes = [
    "C0","C#0","D0","D#0","E0","F0","F#0","G0","G#0","A0","A#0","B0",
    "C1","C#1","D1","D#1","E1","F1","F#1","G1","G#1","A1","A#1","B1",
    "C2","C#2","D2","D#2","E2","F2","F#2","G2","G#2","A2","A#2","B2",
    "C3","C#3","D3","D#3","E3","F3","F#3","G3","G#3","A3","A#3","B3",
    "C4","C#4","D4","D#4","E4","F4","F#4","G4","G#4","A4","A#4","B4",
    "C5","C#5","D5","D#5","E5","F5","F#5","G5","G#5","A5","A#5","B5",
    "C6","C#6","D6","D#6","E6","F6","F#6","G6","G#6","A6","A#6","B6",
    "C7","C#7","D7","D#7","E7","F7","F#7","G7","G#7","A7","A#7","B7",
    "C8","C#8","D8","D#8","E8","F8","F#8","G8","G#8","A8","A#8","B8",
    "C9","C#9","D9","D#9","E9","F9","F#9","G9","G#9","A9","A#9","B9"
];

let noteFrequencies, audioContext, mediaElementAudioSourceNode, analyserNode, dataArray, frequencies = [], changes = [];

fileSelect.addEventListener('input',
    (event) => {
        const urlObj = URL.createObjectURL(event.target.files[0]);
        fileVideo.src = urlObj;
        getNoteFrequencies();
        audioContext = new AudioContext({
            latencyHint: 'interactive',
            sampleRate: 44100
        });
        mediaElementAudioSourceNode = audioContext.createMediaElementSource(fileVideo);
        analyserNode = new AnalyserNode(audioContext, {
            fftSize: 1024
        });
        dataArray = new Uint8Array(analyserNode.frequencyBinCount);
    
        mediaElementAudioSourceNode.connect(audioContext.destination);
        mediaElementAudioSourceNode.connect(analyserNode);
    
        analyserNode.connect(audioContext.destination);

        // setInterval(() => drawVisual(analyserNode, dataArray), 100)
        drawVisual(analyserNode, dataArray);
    }
);

function bandPass(base, top) {
    let newFrequencies = Array.from(dataArray);
    newFrequencies.splice(0, base);
    newFrequencies.splice(top, dataArray.length - top);
    return newFrequencies;
}

function getNoteFrequencies() {
    noteFrequencies = [];
    for (let i = 0; i < notes.length; i++) {
        let relative = i - A4_INDEX;
        noteFrequencies[i] = A4 * Math.pow(STEP, relative);
    }
}

function frequencyToNote(freq) {
    for (let i = 1; i < noteFrequencies.length; i++) {
        // console.log(noteFrequencies[i] - (noteFrequencies[i] - noteFrequencies[i - 1]) / 2, noteFrequencies[i] + (noteFrequencies[i + 1] - noteFrequencies[i]) / 2, freq)
        if (i == 0 && freq <= noteFrequencies[i] - (noteFrequencies[i + 1] - noteFrequencies[i]) / 2) {
            return notes[i];
        }
        if (freq > noteFrequencies[i] - (noteFrequencies[i] - noteFrequencies[i - 1]) / 2 && freq <= noteFrequencies[i] + (noteFrequencies[i + 1] - noteFrequencies[i]) / 2) {
            return notes[i];
        }
    }
}

function analyseChanges(newFrequencies, base, step) {
    let wordAudio = '';
    for (let i = 0; i < newFrequencies.length; i++) {
        if (newFrequencies[i] - frequencies[i] >= 10) {
            changes[i] = newFrequencies[i];

            let note = frequencyToNote(Math.round(base + step * i));
            
            if (note && wordAudio.indexOf(note) == -1) {
                wordAudio += `${note} `;
            }
        }
        else {
            changes[i] = 0;
        }
    }
    if (wordAudio.length > 0) {
        audioFrequencyList.innerHTML = wordAudio;
    }
}

function drawVisual() {
    requestAnimationFrame(
        () => {
            drawVisual();
        }
    );
    analyserNode.getByteFrequencyData(dataArray);
    let step = (audioContext.sampleRate / 2) / dataArray.length;
    let base = Math.floor(16.35 / step);
    let top = Math.ceil(4186.01 / step);
    let newFrequencies = bandPass(base, top);
    analyseChanges(newFrequencies, base, step);
    frequencies = newFrequencies;

    let audioFrequencyCtx = audioFrequency.getContext('2d');
    audioFrequencyCtx.clearRect(0, 0, audioFrequency.width, audioFrequency.height);

    let barWidth = audioFrequency.width / frequencies.length;
    let x = 0;
    for (let volume of frequencies) {
        let barHeight = volume * audioFrequency.height / 255;
        audioFrequencyCtx.fillStyle = '#000';
        audioFrequencyCtx.fillRect(x, audioFrequency.height - barHeight, barWidth / 2, barHeight);
        x += barWidth; 
    }

    barWidth = audioFrequency.width / changes.length;
    x = 0;
    for (let volume of changes) {
        let barHeight = volume * audioFrequency.height / 255;
        audioFrequencyCtx.fillStyle = '#f00';
        audioFrequencyCtx.fillRect(x + barWidth / 2, audioFrequency.height - barHeight, barWidth / 2, barHeight);
        x += barWidth;
    }
}