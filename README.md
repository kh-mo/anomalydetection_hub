# anomalydetection_hub

### Getting Started

1. 가상환경 생성하기
- mac
```bash
pyenv install 3.8.8
pyenv virtualenv 3.8.8 anomalydetection_hub
git clone https://github.com/kh-mo/anomalydetection_hub.git
cd anomalydetection_hub
pyenv activate anomalydetection_hub
```

- windows
```bash
conda create -n anomalydetection_hub python=3.8.8
git clone https://github.com/kh-mo/anomalydetection_hub.git
cd anomalydetection_hub
conda activate anomalydetection_hub
```

2. 패키지 설치하기 & pre-commit 자동화하기
```bash
# 패키지 설치
pip install -r requirements.txt
# pre-commit 자동화
pre-commit install
```

3. 데이터 다운받기

다음과 같은 데이터셋을 data 폴더에 다운로드 받는다.

Dataset list : ucr_time_series_anomaly_archive,

```bash
python download_data.py --name [dataset]
```