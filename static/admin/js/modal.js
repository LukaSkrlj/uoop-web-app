//Inicijalizacija varijabli
<<<<<<< HEAD
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

let vrijeme = 2
let timerTime = vrijeme*60*1000
let idButton = 0
let shuffledQuestions, currentQuestionIndex, maxQuestions
let time = 0;

//Adding actions which are activated on a button click

startQuiz.addEventListener('click', startQuizFunction)
startQuiz.addEventListener('click', closeDialog)
quizFinish.addEventListener('click', alertPopUp)
closeModal2.addEventListener('click', alertPopUp)
=======
const closeModal2Button = document.getElementById('button_closeModal2')
const pokreniKvizButton = document.getElementById('button_pokreniKviz')
const zavrsiKvizButton = document.getElementById('button_zavrsiKviz')
const iducePitanjeButton = document.getElementById('button_iducePitanje')
const timerButton = document.getElementById('timer')
const preostaloVrijemeSpan = document.getElementById('span_preostaloVrijeme')
const ispitImeSpan = document.getElementById('span_ispitIme')
const brojPitanjaSpan = document.getElementById('span_brojZadatka')
const pitanjeDiv = document.getElementById('div_pitanje')
const opcijeOdgovoraDiv = document.getElementById('div_opcijeOdgovora')


const questionContainerElement = document.getElementById('div_pitanje')
const questionElement = document.getElementById('question')
const answerButtonsElement = document.getElementById('answer-buttons')

let vrijeme = 2
let timerVrijeme = vrijeme*60*1000

let shuffledQuestions, currentQuestionIndex, maxQuestions
let time = 0;

//Dodavanje akcija koje se pokreću dodirom gumba

pokreniKvizButton.addEventListener('click', startGame)
pokreniKvizButton.addEventListener('click', closeDialog)
zavrsiKvizButton.addEventListener('click', alertPopUp)
closeModal2Button.addEventListener('click', alertPopUp)
>>>>>>> 6c517cb (File sa javascript kodom za teorijski kviz)


//Alert box 
function alertPopUp() {
  var txt
  if (confirm("Jeste li sigurni da želite završiti kviz")) {
    closeQuiz()   
  } else {
    //
  }
}
<<<<<<< HEAD
//Showing left time in timer
//TO DO:display timer with 2 digits
function timeLeftFunction(){
	if(timerTime == 0){closeQuiz()}
	if(timerTime == 60*1000){timer.style.background = 'red'}
	let minutes = Math.floor(timerTime/60/1000)
	let seconds = Math.floor(timerTime - (minutes*60*1000)) / 1000 
	timeLeft.innerText = String(minutes) + ':' + String(seconds)
	timerTime -= 1000
	
}

//Function activated by nextButton
nextQuestion.addEventListener('click', () => {
  currentQuestionIndex++
  setNextQuestion()
})
//Co
=======
//prikaz preostalog vremena u timeru
//TO DO:prikaz s 2 brojke
function timeLeft(){
	if(timerVrijeme == 0){closeQuiz()}
	if(timerVrijeme == 60*1000){timer.style.background = 'red'}
	let minute = Math.floor(timerVrijeme/60/1000)
	let sekunde = Math.floor(timerVrijeme - (minute*60*1000)) / 1000 
	preostaloVrijemeSpan.innerText = String(minute) + ':' + String(sekunde)
	timerVrijeme -= 1000
	
}

//funkcija koja se pokreće klikom na button iduće pitanje
iducePitanjeButton.addEventListener('click', () => {
  currentQuestionIndex++
  setNextQuestion()
})
//zatvaranje informativnog modala
>>>>>>> 6c517cb (File sa javascript kodom za teorijski kviz)
function closeDialog() {
		$("#exampleModal").modal('hide');
		$('body').removeClass('modal-open');
		$('.modal-backdrop').remove(); 
    }
	
//zatvaranje modala s kvizom
function closeQuiz() {
		$("#staticBackdrop").modal('hide');
		$('body').removeClass('modal-open');
		$('.modal-backdrop').remove(); 
<<<<<<< HEAD
    $("#openInfoModal").hide();
   }


//funkcija koja provjerava je li unesen odgovor točan
//TO DO: uncheck radio buttona
function checkCorrect(){
	Array.from(answers.children).forEach(button => {
    
  })
  if (shuffledQuestions.length > currentQuestionIndex + 1) {
    nextQuestion.classList.remove('hide')
=======
    }
	
//funkcija koja provjerava je li unesen odgovor točan
//TO DO: uncheck radio buttona
function checkCorrect(){
	Array.from(opcijeOdgovoraDiv.children).forEach(button => {
    
  })
  if (shuffledQuestions.length > currentQuestionIndex + 1) {
    iducePitanjeButton.classList.remove('hide')
>>>>>>> 6c517cb (File sa javascript kodom za teorijski kviz)
  } 
	
}

//početna funkcija prilikom pokretanja kviza
<<<<<<< HEAD
function startQuizFunction() {
  setInterval(timeLeftFunction, 1000); //periodično dekrementiranje timera
  startQuiz.classList.add('hide') //skrivanje buttona
  shuffledQuestions = questions.sort(() => Math.random() - .5) 
  currentQuestionIndex = 0
  maxQuestions = 4;
 // question.classList.remove('hide')
=======
function startGame() {
  setInterval(timeLeft, 1000); //periodično dekrementiranje timera
  pokreniKvizButton.classList.add('hide') //skrivanje buttona
  shuffledQuestions = questions.sort(() => Math.random() - .5) 
  currentQuestionIndex = 0
  maxQuestions = 4;
  questionContainerElement.classList.remove('hide')
>>>>>>> 6c517cb (File sa javascript kodom za teorijski kviz)
  setNextQuestion()
}

//postavljanje idućeg pitanja i skrivanje buttona ako je zadnje pitanje u kvizu
function setNextQuestion() {
  checkCorrect()
  resetState()
  if(currentQuestionIndex == maxQuestions -1){
<<<<<<< HEAD
	  nextQuestion.style.visibility = 'hidden'
=======
	  iducePitanjeButton.style.visibility = 'hidden'
>>>>>>> 6c517cb (File sa javascript kodom za teorijski kviz)
  }
  
	showQuestion(shuffledQuestions[currentQuestionIndex]);
	 
}

//prikaz pitanja i radio buttona i njihovih tekstova
<<<<<<< HEAD
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
  
=======
function showQuestion(question) {
	pitanjeDiv.innerText = question.question
	brojPitanjaSpan.innerText = currentQuestionIndex +1
	question.answers.forEach(answer => {
    const button = document.createElement('INPUT')
	button.setAttribute("type", "radio")
    button.classList.add('btn')
	button.setAttribute("label", answer.text)
>>>>>>> 6c517cb (File sa javascript kodom za teorijski kviz)
	
	const y = document.createElement("LABEL")
	const t = document.createTextNode(' ' + answer.text)
	y.textContent = "Label text"
	y.setAttribute("for", "lord")
	
	linebreak = document.createElement("br")
		
    if (answer.correct) {
      button.dataset.correct = answer.correct
	  
    }
	
	//dodavanje novih elemenata u div->dinamično mijenjanje broja radio buttona
<<<<<<< HEAD
  button.addEventListener('click', selectAnswer)
  answers.appendChild(button)
	answers.appendChild(t)
	answers.appendChild(linebreak)
=======
    button.addEventListener('click', selectAnswer)
    opcijeOdgovoraDiv.appendChild(button)
	opcijeOdgovoraDiv.appendChild(t)
	opcijeOdgovoraDiv.appendChild(linebreak)
>>>>>>> 6c517cb (File sa javascript kodom za teorijski kviz)
  })
}

//reset modala kako bi se u modalu izbrisalo staro pitanje i radio buttoni
function resetState() {
  clearStatusClass(document.body)
<<<<<<< HEAD
  nextQuestion.classList.add('hide')
  while (answers.firstChild) {
    answers.removeChild(answers.firstChild)
=======
  iducePitanjeButton.classList.add('hide')
  while (opcijeOdgovoraDiv.firstChild) {
    opcijeOdgovoraDiv.removeChild(opcijeOdgovoraDiv.firstChild)
>>>>>>> 6c517cb (File sa javascript kodom za teorijski kviz)
  }
}

//odabir odgovora, postavljanje točnosti u button dataset iz questions arraya
function selectAnswer(e) {
  const selectedButton = e.target
  const correct = selectedButton.dataset.correct
  setStatusClass(document.body, correct)
<<<<<<< HEAD
  Array.from(answers.children).forEach(button => {
    setStatusClass(button, button.dataset.correct)
  })
  if (shuffledQuestions.length > currentQuestionIndex + 1) {
    nextQuestion.classList.remove('hide')
=======
  Array.from(opcijeOdgovoraDiv.children).forEach(button => {
    setStatusClass(button, button.dataset.correct)
  })
  if (shuffledQuestions.length > currentQuestionIndex + 1) {
    iducePitanjeButton.classList.remove('hide')
>>>>>>> 6c517cb (File sa javascript kodom za teorijski kviz)
  } 
}

//dodavanje u listu točnih i netočnih
//TO DO: brojač točnih i netočnih pitanja na temelju baze podataka kako se reloadom ne bi izgubili podaci
function setStatusClass(element, correct) {
  clearStatusClass(element)
  if (correct) {
    element.classList.add('correct')
  } else {
    element.classList.add('wrong')
  }
}

//micanje točnih i netočnih odgovora iz liste, kako bi se iduće pitanje ispravno izvršavalo
function clearStatusClass(element) {
  element.classList.remove('correct')
  element.classList.remove('wrong')
}

//Array s pitanjima i ponuđenim odgovorima
//TO DO:umjesto arraya ubaciti povezivanje s bazom podataka
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
