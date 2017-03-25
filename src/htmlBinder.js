function bindButtons() {
  $( ".answerButton" ).click(function() {
    answer($(this)[0].innerText)
  });
}

function inputAnswers(answers) {
  const prototype = "<div class=\"answerButton\"></div>"
  const ans1 = $(prototype).html(answers[0])
  const ans2 = $(prototype).text(answers[1])
  const ans3 = $(prototype).text(answers[2])
  const ans4 = $(prototype).text(answers[3])
  $( ".answerContainer" ).html("")
  $( ".answerContainer" ).append(ans1, ans2, ans3, ans4)
  bindButtons()
}

function showWin(message) {
  const prototype = "<div class=\"splashContent win\"></div>"
  const splash = $(prototype).html(message)
  $(".verticalWrapper").html(splash)
}

function showLose(message) {
  const prototype = "<div class=\"splashContent lose\"></div>"
  const splash = $(prototype).html(message)
  $(".verticalWrapper").html(splash)
}

function createUrl(path, format) {
  path[path.length-1] = format
  return path.join('.')
}

function setMedia(url) {
  const prototypeImg = "<img id=\"questionImage\" src=\"\"></img>"
  var split = url.split('.')
  var media = $(prototypeImg).attr("src", url)
  if (split[split.length-1] === 'gifv' || split[split.length-1] === 'mp4' ) {
    const prototypeVideo = '<video preload="auto" autoplay="autoplay" loop="loop" id="questionImage"></video>'
    const prototypeSource = '<source src="" type="video/webm"></source>'
    urlwebm = createUrl(split, 'webm')
    urlmp4 = createUrl(split, 'mp4')
    const source = $(prototypeSource).attr("src", urlwebm)
    const source2 = $(prototypeSource).attr("src", urlmp4)
    media = $(prototypeVideo).html(source).append(source2)
  }
  $('#questionMedia').html(media)
}
