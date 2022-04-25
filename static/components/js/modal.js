
//Variable initilization
const closeModal2 = document.getElementById('closeModal2')
const startQuiz = document.getElementById('quizStart')
const quizFinish = document.getElementById('quizFinish')
const nextQuestion = document.getElementById('nextQuestion')
const timer = document.getElementById('timer')
const timeLeft = document.getElementById('timeLeft')
const quizName = document.getElementById('quizName')
const questionNumber = document.getElementById('questionNumber')
const question = document.getElementById('question')
const answers = document.getElementById('answers')

let timerTime = ((((String)(maxMinutes)-(String)(minMinutes)) * 60) + ((String)(maxSeconds)-(String)(minSeconds))) * 1000;

let idButton = 0;
let shuffledQuestions, currentQuestionIndex, maxQuestions;
let time = 0;


//Adding actions which are activated on a button click

startQuiz.addEventListener('click', startQuizFunction)
startQuiz.addEventListener('click', closeDialog)
quizFinish.addEventListener('click', alertPopUp)
closeModal2.addEventListener('click', alertPopUp)


//Alert box 
function alertPopUp() {
  var txt
  if (confirm("Jeste li sigurni da želite završiti kviz")) {
    closeQuiz()   
  } else {
    //
  }
}
//Showing left time in timer
//TO DO:display timer with 2 digits
function timeLeftFunction(){
if(timerTime == 0){closeQuiz()}
	else if(timerTime == 60*1000){timer.style.background = 'red'}
  let minute = Math.floor(timerTime/60/1000)
	let second = Math.floor(timerTime - (minute*60*1000)) / 1000 
  timeLeft.innerText = String(minute) + ':' + String(second)
	timerTime -= 1000
}


//Function activated by nextButton
nextQuestion.addEventListener('click', () => {
  currentQuestionIndex++
  setNextQuestion()
})
//Close background
function closeDialog() {
		$("#exampleModal").modal('hide');
		$('body').removeClass('modal-open');
		$('.modal-backdrop').remove(); 
    }
	
//closing modal with quiz
function closeQuiz() {
		$("#staticBackdrop").modal('hide');
		$('body').removeClass('modal-open');
		$('.modal-backdrop').remove(); 
    $("#openInfoModal").hide();
   }


//function which checks if the answer is correct
//TO DO: uncheck radio buttons
function checkCorrect(){
	Array.from(answers.children).forEach(button => {
    
  })
  if (shuffledQuestions.length > currentQuestionIndex + 1) {
    nextQuestion.classList.remove('hide')
  } 
	
}

//start function for quiz
function startQuizFunction() {
  setInterval(timeLeftFunction, 1000); //periodic timera decrement
  startQuiz.classList.add('hide') //button hiding
  shuffledQuestions = questions.sort(() => Math.random() - .5) 
  currentQuestionIndex = 0
  maxQuestions = 4;
  setNextQuestion()
}

//setting next question and checking if a question is the last one in the quiz
function setNextQuestion() {
  checkCorrect()
  resetState()
  if(currentQuestionIndex == maxQuestions -1){
	  nextQuestion.style.visibility = 'hidden'
  }
  
	showQuestion(shuffledQuestions[currentQuestionIndex]);
	 
}

//diplaying radio buttons and available answers
function showQuestion(questionvariable) {
	question.innerText = questionvariable.question
	questionNumber.innerText = currentQuestionIndex +1
  let nameOfGroup = "zadatak" + currentQuestionIndex

	questionvariable.answers.forEach(answer => {
  const button = document.createElement('INPUT')
	button.setAttribute("type", "radio")
  
  $( "button.continue" ).html( "Next Step..." )
  button.classList.add('btn')
	button.setAttribute("label", answer.text)
  button.setAttribute("name",nameOfGroup)
  button.setAttribute("id", answer.text);
  
	
	const y = document.createElement("LABEL")
	const t = document.createTextNode(' ' + answer.text)
	y.textContent = "Label text"
	y.setAttribute("for", "lord")
	
	linebreak = document.createElement("br")
		
    if (answer.correct) {
      button.dataset.correct = answer.correct
	  
    }
	
	//adding new elements in div->dynamically changes the number of radio buttons
  button.addEventListener('click', selectAnswer)
  answers.appendChild(button)
	answers.appendChild(t)
	answers.appendChild(linebreak)
  })
}

//resets modal to delete existing question and radio buttons from last question
function resetState() {
  clearStatusClass(document.body)
  nextQuestion.classList.add('hide')
  while (answers.firstChild) {
    answers.removeChild(answers.firstChild)
  }
}

//choosing answer, putting true/false to button dataset from questions array
function selectAnswer(e) {
  const selectedButton = e.target
  const correct = selectedButton.dataset.correct
  setStatusClass(document.body, correct)
  Array.from(answers.children).forEach(button => {
    setStatusClass(button, button.dataset.correct)
  })
  if (shuffledQuestions.length > currentQuestionIndex + 1) {
    nextQuestion.classList.remove('hide')
  } 
}

//adding to correct/false list
//TO DO: counter of correct/false answers connected to the database so data is not lost by page reload
function setStatusClass(element, correct) {
  clearStatusClass(element)
  if (correct) {
    element.classList.add('correct')
  } else {
    element.classList.add('wrong')
  }
}

//removing correct/false answers so the next question can function normally
function clearStatusClass(element) {
  element.classList.remove('correct')
  element.classList.remove('wrong')
}

//Array with questions and answers
//TO DO:connection with database instead of array
const questions = [
  {
    question: 'Statičke metode ne mogu pristupiti ni jednom članu klase koji također nije statičan',
    answers: [
      { text: 'Točno', correct: true },
      { text: 'Netočno', correct: false }
    ]
  },
  {
	  
    question: 'Prednosti Jave su:',
    answers: [
      { text: 'Može se izvoditi bez preinaka na svim operacijskim sustavima za koje postoji JVM', correct: true },
      { text: 'Bogati skup klasa za rad s mrežnim komunikacijama u jednom trenutku', correct: true },
      { text: 'Podržava višestruko nasljeđivanje klasa', correct: false },
      { text: 'Svaka klasa i njezine metode imaju definirane modifikatore pristupa', correct: true }
    ]
  },
  {
    question: 'Odaberi točna rješenja',
    answers: [
      { text: 'Datoteke izvornog koda moraju biti imenovane prema javnoj klasi koju sadrže', correct: true },
      { text: 'Modifikatori pristupa ograničavaju tko sve smije pozvati metode i tko ima pristup varijablama klase', correct: true },
      { text: 'void označava da funkcija na koncu izvođenja ne vraća nikakvu vrijednost onome tko ju je pozvao', correct: true },
      { text: 'Statičke metode mogu pristupiti jednom članu klase koji nije statičan', correct: false }
    ]
  },
  {
    question: 'Java je objektno orijentiran jezik',
    answers: [
      { text: 'Točno', correct: true },
      { text: 'Netočno', correct: false }
    ]
  }
]
