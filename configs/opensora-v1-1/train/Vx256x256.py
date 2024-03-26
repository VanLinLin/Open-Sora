# Define dataset
data_path = "CSV_PATH"
num_frames = 16
frame_interval = 3
image_size = (256, 256)

# Define acceleration
num_workers = 4
dtype = "bf16"
grad_checkpoint = True
plugin = "zero2"
sp_size = 1

# Define model
model = dict(
    type="STDiT2-XL/2",
    space_scale=0.5,
    from_pretrained="PixArt-XL-2-1024-MS.pth",
    enable_flashattn=True,
    enable_layernorm_kernel=True,
)
vae = dict(
    type="VideoAutoencoderKL",
    from_pretrained="stabilityai/sd-vae-ft-ema",
    micro_batch_size=4,
)
text_encoder = dict(
    type="t5",
    from_pretrained="DeepFloyd/t5-v1_1-xxl",
    model_max_length=120,
    shardformer=True,
)
scheduler = dict(
    type="iddpm-speed",
    timestep_respacing="",
)

# Others
seed = 42
outputs = "outputs"
wandb = False

epochs = 1000
log_every = 10
ckpt_every = 1000
load = None

batch_size = 8
lr = 2e-5
grad_clip = 1.0