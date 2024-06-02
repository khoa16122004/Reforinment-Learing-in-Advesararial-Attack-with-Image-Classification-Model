from collections import namedtuple

CLASSIFIER_ARCH = "vgg16"
CLASSIFIER_TRAINED = "Trained_model\classifier_cifar10.pth"
DATASET = "cifar10_splits"
BATCH_SIZE = 32
EPS = 20
EPSILON = 0.1
IMG_SIZE = 32 # areas: img_size ^ 2
MASK_SIZE = 4 # areas: mask_size ^ 2
NUM_MASKS = 10 

MAX_ITER = 600
NOISE_SD = 0.005
GAMMA = 0.9
TARGET_UPDATE = 1000

INPUT_DQN_SIZE = 580 # 512 + 64 + 4
OUTPUT_DQN_SIZE = 64
DQN_TRAINED = "model_0.pth"
TRACK_FOLDER = "view"
TEST_FOLDER = "view_test"
ACTION_TRACK = "actions.json"
LOSS_TRACK = "losses.json"
REWARD_TRACK = "rewards.json"

Transition = namedtuple('Transition',
                        ('state', 'action', 'next_state', 'reward'))