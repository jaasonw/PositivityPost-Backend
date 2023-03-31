import warnings

warnings.filterwarnings("ignore", category=FutureWarning)
from summarizer import Summarizer, TransformerSummarizer
import newspaper

urls = [
    "https://abc7.com/trump-indictment-what-happens-after-next-steps/13052759/",
    "https://abc7.com/donald-trump-indictment-reaction-republicans-jim-jordan/13052865/",
    "https://abc7.com/snowboarder-buried-alive-upside-down-saved-snow/13050849/",
    "https://www.cnbc.com/2023/03/31/chinas-banking-troubles-not-the-same-as-silicon-valley-bank-economist.html",
    "https://www.nytimes.com/2023/03/30/world/europe/finland-nato-turkey.html",
]

GPT2_model = TransformerSummarizer(
    transformer_type="GPT2", transformer_model_key="gpt2-medium"
)

for url in urls:
    print(url)
    article = newspaper.Article(url=url, language="en")
    article.download()
    article.parse()
    print(str(article.title))
    full = "".join(GPT2_model(str(article.text), min_length=60))
    print(full)
    print()
    print()
    print()
