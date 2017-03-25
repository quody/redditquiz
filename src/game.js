var score = 0
var totalAnswers = 0
var currentQuestion = {}
const choiceCount = 4;

console.log("Game started")

function start() {
  loadQuestion()
  inputAnswers(loadAnswers())
  //Init score?
  //Start timer?
}

function loadQuestion() {
  currentQuestion = selectImage()
  setMedia(currentQuestion.url)
}


function loadAnswers() {
  answers = []
  answers.push(randomSub())
  answers.push(randomSub())
  answers.push(randomSub())
  answers.push(randomSub())
  answers[Math.floor(Math.random() * choiceCount)] = currentQuestion.sub
  return answers
}

function randomSub() {
  return subs[Math.floor(Math.random() * subs.length)]
}

function win() {
  score += 1
  totalAnswers += 1
  showWin("Correct!")
  setTimeout(start, 500)
}

function lose() {
  totalAnswers += 1
  showLose("Noob!")
  setTimeout(start, 500)
}

function answer(name) {
  if (name === currentQuestion.sub) { // Handle caps
    console.log("winned")
    win()
    selectImage()
  }
  else {
    console.log("lossed", currentQuestion.sub)
    lose()
    selectImage()
  }
}
