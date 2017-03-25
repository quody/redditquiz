var treeData = []
var subs = []
a = "Replace from here"
/*$.getJSON('../data/images2.json', function(json) {
  treeData = treeData.concat(json)
})
$.getJSON('../data/images3.json', function(json) {
  treeData = treeData.concat(json)
})*/
$.getJSON('../data/images.json', function(json) {
  console.log("Loaded images")
  treeData = treeData.concat(json)
})
a = "Replace from here"
$( document ).ready(function () {
  parseSubs()
  start()
})

function parseSubs() {
  for( var i = 0; i < treeData.length; i++) {
    subs.push(treeData[i].sub)
  }
}

function selectImage() {
  var imageId = Math.floor( treeData.length * Math.random() )
  return treeData[imageId]
}
