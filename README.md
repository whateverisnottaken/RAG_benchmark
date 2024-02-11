# RAG_benchmark
This is a benchmark for evaluating RAG tools, for both general tasks and comprehensive tasks.
## benchmarks
This benchmark repository contains 3 parts of scores:

1. It calculates the recall of your recall model on top 1, top 3, top 5 and top 10 retrieval results.
2. It calculates how well your model can tell if the information is contained within the contexts.
3. It shows the inference results of your RAG tool and you can score it artificially.

# How To Use
## Step 1:
Make sure you have Python >= 3.8 on your device.
## Step 2:
run `pip install -r requirements.txt`
## Step 3:
Implement all 3 functions in `custom_test.py`
## Step 4:
run `python score.py` and see your result.
# Explaination on Dataset
This dataset includes texts from wikipedia and question-answer pairs in Japanese.
## Example of general tasks:
`Question: 山手線はどの会社が運営していますか？`
`Answer: 東日本旅客鉄道（JR東日本）が運営しています。`
## Example of comprehensive tasks:
`Question: 尼崎市に本社を置く企業の共通点とは何ですか？`
`Answer: 尼崎市に本社を置いた企業は、歴史があり、また地域に密接している企業であるという共通点があります。例えば、ユニチカは1889年に尼崎紡績が前身となり設立された歴史ある企業であり、阪神電気鉄道は一時期尼崎に本社を設置していたことが挙げられます。さらにエディオンの前身企業のミドリ電化は本社を尼崎に置き、洋菓子のヒロタやコンフェクショナリーコトブキも市内に本社工場を構え、深いつながりを持っています。また、ヤンマーディーゼルサッカー部は、現在はセレッソ大阪となっていますが、その起源を尼崎市に持っています。`
# How to implement `custom_test.py`
Please refer to the comments in the script. A simple example is also presented.
