import torch
import os
import Preprosse
from Create_Hparams import Create_Prepro_Hparams, Create_Train_Hparams
import librosa
from MydataSet import pad, segment
from Model import Classifier
import Trainer


def load_model(path, hp: Create_Train_Hparams):
    if not os.path.exists(path):
        print('{}路径不存在'.format(path))
    else:
        return torch.load(path)


def create_model_path(ver, checkpoint=6):
    ponits = ['000199.pth', '000399.pth', '000599.pth', '000799.pth', '000999.pth', '001199.pth', '001399.pth',
              '001501.pth']
    path = './Experiments/{}/checkpoints_{}/{}'.format(ver, ver, ponits[checkpoint])
    return path


def extract_mel(vi_input_path, hp: Create_Prepro_Hparams):
    stftfunc = Preprosse.TacotronSTFT(filter_length=hp.n_fft,  ###1024
                                      hop_length=hp.hop_length,  ## 256
                                      win_length=hp.win_length,  ###1024
                                      n_mel_channels=hp.n_mels,  ### 80
                                      sampling_rate=hp.sample_rate,  ###22050 different from tacotron2 22050
                                      mel_fmin=hp.f_min,  ## 0.0
                                      mel_fmax=hp.f_max)  ## 11025

    wavform, _ = librosa.load(vi_input_path)
    wavform, _ = librosa.effects.trim(wavform, top_db=10)
    wavform = torch.FloatTensor(wavform).unsqueeze(0)
    mel = stftfunc.mel_spectrogram(wavform)
    return mel


if __name__ == '__main__':
    ver = 'v1'
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    hpt = Create_Train_Hparams()
    model_path = create_model_path(ver, checkpoint=7)
    model = load_model(model_path, hpt)
    wav_path = ''
    hpp = Create_Prepro_Hparams()
    mel = extract_mel(wav_path, hpp).squeeze()
    mel = torch.FloatTensor(segment(mel, 128))
    mel = mel.unsqueeze(0)
    mel = mel.unsqueeze(0)
    mel = mel.transpose(2, 3)
    mel = mel.to(device)
    label = model(mel)
    print()
