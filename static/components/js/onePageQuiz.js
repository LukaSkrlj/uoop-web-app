//Variable initilization
const closeModal2 = document.getElementById('closeModal2')
const startQuiz = document.getElementById('quizStart')
const quizFinish = document.getElementById('quizFinish')
const timer = document.getElementById('timer')
const timeLeft = document.getElementById('timeLeft')
//const quizName = document.getElementById('quizName')
//const questionNumber = document.getElementById('questionNumber')
const question = document.getElementById('question')
const answers = document.getElementById('answers')

let timerTime = ((((String)(maxMinutes)-(String)(minMinutes)) * 60) + ((String)(maxSeconds)-(String)(minSeconds))) * 1000;




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


//start function for quiz
function startQuizFunction() {
  setInterval(timeLeftFunction, 1000); //periodic timera decrement
  startQuiz.classList.add('hide') //button hiding
}


