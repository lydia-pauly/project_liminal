# data
image_size = 256

# KID = Kernel Inception Distance, see related section
kid_image_size = 75
kid_diffusion_steps = 5

# sampling
min_signal_rate = 0.02
max_signal_rate = 0.95

# architecture
embedding_dims = 32
embedding_max_frequency = 1000.0
widths = [32, 64, 96, 128]
block_depth = 2

# optimization
batch_size = 6
ema = 0.999
learning_rate = 1e-3
weight_decay = 1e-4
