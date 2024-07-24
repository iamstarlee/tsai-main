import torch
import torch.nn as nn
import numpy as np
np.set_printoptions(threshold=np.inf)

# Define the neural network
class SimpleConv1DNet(nn.Module):
    def __init__(self):
        super(SimpleConv1DNet, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=1, out_channels=16, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(16 * 70, 10)  # Fully connected layer

    def forward(self, x):
        x = self.conv1(x)  # Apply the Conv1D layer
        print(f"x is {x}")
        x = torch.relu(x)  # Apply ReLU activation
        x = x.view(x.size(0), -1)  # Flatten the output for the fully connected layer
        x = self.fc1(x)  # Apply the fully connected layer
        return x

# Create a sample 1x70 time series input
time_series = np.loadtxt("raw_data/y.txt")  # Batch size 1, 1 channel, 70 data points
time_series = torch.from_numpy(time_series).float()
time_series = torch.unsqueeze(time_series, 0)
time_series = torch.unsqueeze(time_series, 0)
print(f"Shape is {time_series}")

# Instantiate the model
model = SimpleConv1DNet()

# Forward pass
output = model(time_series)

# Print the output
print(output)
