
# Fake News Detection 

With tremendous amount of data flowing over internet, most of them are found
fake but still people prefer the internet source as it is the easiest means. Unfortunately the open source has become the platform to release news without effective
supervision. Fake news are delivered cleverly in a traditional method that implies
to be truthful but contain misleading information. By utilizing different philosophies, realizing the correctness of the news is a fascinating issue.

## Content
The following files are included:
| Folder / File | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Dataset`      | `folder` | Contains Pre-processed dataset |
| `FakeNewsDetection`      | `Backend Folder` | django based backend system for our project |
| `Project Demo`      | `Video file` | Contains video of how our project works |
| `Research Paper`      | `files` | All the resesearch paper we referenced for our project |
| `Frontend`      | `folder` | UI of our Frontend  |
| `requirements.txt`      | `file` | **Required**. Python Library required for the projects |


## How to Use This Script ?
To clone our project,
```bash
  git clone git@github.com:XDSushanO/FakeNewsPrediction.git
```

Foremost thing is you need to install the requirements so you could run everything. This repository contains a requirements.txt

To install requirements.txt

```bash
  pip install -r requirements.txt
```

To run the Fake News Detection,

First change the directory to FakeNewsDetection
```bash
  cd FakeNewsDetection
```
And, run server
```bash
  py manage.py runserver
```
Go to local host server on the browser of your choice
```bash
 127.0.0.1:8000
