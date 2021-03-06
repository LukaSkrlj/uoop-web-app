//Variable initilization
const startQuiz = document.getElementById('quizStart')
const quizFinish = document.getElementById('quizFinish')
const timer = document.getElementById('timer')
const timeLeft = document.getElementById('timeLeft')



//Adding actions which are activated on a button click

startQuiz.addEventListener('click', startQuizFunction)
startQuiz.addEventListener('click', closeDialog)
quizFinish.addEventListener('click', submitClicked)

//Making time object with info about quiz submit time from database
var finishTime = new Date(Date.UTC(maxYears, maxMonths-1, maxDays, maxHours, maxMinutes, maxSeconds, maxMilliseconds));//month-1 because months are in a span 0-11
var countDownDate = finishTime.getTime(); //converting time to miliseconds
var distance = 0 


function calculateTimeLeft(){
  // Returns the value of current day and time
  var now = new Date().getTime();

  // Find the distance between now and the final quiz submit date
  distance = countDownDate - now ;

  // Time calculations for days, hours, minutes and seconds left
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);
  
  // Displays the result in the timer
  if(days > 0){
    timeLeft.innerText =  days + ":" + hours + ":" + minutes + ":" + seconds ;}
  else if(hours > 0){
    timeLeft.innerText =  hours + ":" + minutes + ":" + seconds ;}
  else{
    timeLeft.innerText =  minutes + ":" + seconds ;}

  // If the count down is finished
  if (distance <= 0) {
    quizFinish.click();
    clearInterval(x);
    timeLeft.innerHTML = "0:0";
  }
}



//Alert box that lets student confirm quiz submit
function alertPopUp() {
  var txt
  if (confirm("Jeste li sigurni da želite završiti kviz")) {
    closeQuiz(); 
  } else {
    //
  }
}
//if available time has passsed close the quiz or allow student to go back to quiz
function submitClicked(){
  if(distance > 0){
    alertPopUp();
  }
  else{
    closeQuiz();
  }
}

//Close background of info modal
function closeDialog() {
		$("#exampleModal").modal('hide');
		$('body').removeClass('modal-open');
		$('.modal-backdrop').remove(); 
    return;
    }
	
//closing modal with quiz
function closeQuiz() {
		$("#staticBackdrop").modal('hide');
		$('body').removeClass('modal-open');
		$('.modal-backdrop').remove(); 
    $("#openInfoModal").hide();

  }


//start function for timer, removes Start Quiz button
function startQuizFunction() {
  setInterval(calculateTimeLeft, 1000); //periodic timera decrement
  startQuiz.classList.add('hide') //button hiding
}