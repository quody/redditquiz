var treeData
var subs = []
$.getJSON('../data/images.json', function(json) {
  console.log("Loaded images")
  treeData = json
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
