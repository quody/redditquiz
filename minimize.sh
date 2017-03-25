cat ./src_large/data/images.json > ./src/images.json
cat ./src_large/thirdparty/jquery-3.2.0.min.js > ./src/mini.js
cat ./src_large/src/imageloader.js >> ./src/mini.js
cat ./src_large/src/game.js >> ./src/mini.js
cat ./src_large/src/htmlBinder.js >> ./src/mini.js

cp ./src_large/index.html ./src/index.html
cp ./src_large/styles/main.css ./src/styles/main.css

gulp

python pyMinimize.py
