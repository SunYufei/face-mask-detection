import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

__weights_dict = dict()


def load_weights(weight_file):
    if weight_file is None:
        return

    try:
        weights_dict = np.load(weight_file).item()
    except:
        weights_dict = np.load(weight_file, encoding='bytes').item()

    return weights_dict


class KitModel(nn.Module):

    def __init__(self, weight_file):
        super(KitModel, self).__init__()
        global __weights_dict
        __weights_dict = load_weights(weight_file)

        self.conv2d_0 = self.__conv(2, name='conv2d_0', in_channels=3, out_channels=32, kernel_size=(3, 3),
                                    stride=(1, 1), groups=1, bias=False)
        self.conv2d_0_bn = self.__batch_normalization(2, 'conv2d_0_bn', num_features=32, eps=0.0010000000474974513,
                                                      momentum=0.0)
        self.conv2d_1 = self.__conv(2, name='conv2d_1', in_channels=32, out_channels=64, kernel_size=(3, 3),
                                    stride=(1, 1), groups=1, bias=False)
        self.conv2d_1_bn = self.__batch_normalization(2, 'conv2d_1_bn', num_features=64, eps=0.0010000000474974513,
                                                      momentum=0.0)
        self.conv2d_2 = self.__conv(2, name='conv2d_2', in_channels=64, out_channels=64, kernel_size=(3, 3),
                                    stride=(1, 1), groups=1, bias=False)
        self.conv2d_2_bn = self.__batch_normalization(2, 'conv2d_2_bn', num_features=64, eps=0.0010000000474974513,
                                                      momentum=0.0)
        self.conv2d_3 = self.__conv(2, name='conv2d_3', in_channels=64, out_channels=64, kernel_size=(3, 3),
                                    stride=(1, 1), groups=1, bias=False)
        self.conv2d_3_bn = self.__batch_normalization(2, 'conv2d_3_bn', num_features=64, eps=0.0010000000474974513,
                                                      momentum=0.0)
        self.cls_0_insert_conv2d = self.__conv(2, name='cls_0_insert_conv2d', in_channels=64, out_channels=64,
                                               kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.loc_0_insert_conv2d = self.__conv(2, name='loc_0_insert_conv2d', in_channels=64, out_channels=64,
                                               kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv2d_4 = self.__conv(2, name='conv2d_4', in_channels=64, out_channels=128, kernel_size=(3, 3),
                                    stride=(1, 1), groups=1, bias=False)
        self.cls_0_insert_conv2d_bn = self.__batch_normalization(2, 'cls_0_insert_conv2d_bn', num_features=64,
                                                                 eps=0.0010000000474974513, momentum=0.0)
        self.loc_0_insert_conv2d_bn = self.__batch_normalization(2, 'loc_0_insert_conv2d_bn', num_features=64,
                                                                 eps=0.0010000000474974513, momentum=0.0)
        self.conv2d_4_bn = self.__batch_normalization(2, 'conv2d_4_bn', num_features=128, eps=0.0010000000474974513,
                                                      momentum=0.0)
        self.cls_0_conv = self.__conv(2, name='cls_0_conv', in_channels=64, out_channels=8, kernel_size=(3, 3),
                                      stride=(1, 1), groups=1, bias=True)
        self.loc_0_conv = self.__conv(2, name='loc_0_conv', in_channels=64, out_channels=16, kernel_size=(3, 3),
                                      stride=(1, 1), groups=1, bias=True)
        self.cls_1_insert_conv2d = self.__conv(2, name='cls_1_insert_conv2d', in_channels=128, out_channels=64,
                                               kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.loc_1_insert_conv2d = self.__conv(2, name='loc_1_insert_conv2d', in_channels=128, out_channels=64,
                                               kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv2d_5 = self.__conv(2, name='conv2d_5', in_channels=128, out_channels=128, kernel_size=(3, 3),
                                    stride=(1, 1), groups=1, bias=False)
        self.cls_1_insert_conv2d_bn = self.__batch_normalization(2, 'cls_1_insert_conv2d_bn', num_features=64,
                                                                 eps=0.0010000000474974513, momentum=0.0)
        self.loc_1_insert_conv2d_bn = self.__batch_normalization(2, 'loc_1_insert_conv2d_bn', num_features=64,
                                                                 eps=0.0010000000474974513, momentum=0.0)
        self.conv2d_5_bn = self.__batch_normalization(2, 'conv2d_5_bn', num_features=128, eps=0.0010000000474974513,
                                                      momentum=0.0)
        self.cls_1_conv = self.__conv(2, name='cls_1_conv', in_channels=64, out_channels=8, kernel_size=(3, 3),
                                      stride=(1, 1), groups=1, bias=True)
        self.loc_1_conv = self.__conv(2, name='loc_1_conv', in_channels=64, out_channels=16, kernel_size=(3, 3),
                                      stride=(1, 1), groups=1, bias=True)
        self.cls_2_insert_conv2d = self.__conv(2, name='cls_2_insert_conv2d', in_channels=128, out_channels=64,
                                               kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.loc_2_insert_conv2d = self.__conv(2, name='loc_2_insert_conv2d', in_channels=128, out_channels=64,
                                               kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv2d_6 = self.__conv(2, name='conv2d_6', in_channels=128, out_channels=64, kernel_size=(3, 3),
                                    stride=(1, 1), groups=1, bias=False)
        self.cls_2_insert_conv2d_bn = self.__batch_normalization(2, 'cls_2_insert_conv2d_bn', num_features=64,
                                                                 eps=0.0010000000474974513, momentum=0.0)
        self.loc_2_insert_conv2d_bn = self.__batch_normalization(2, 'loc_2_insert_conv2d_bn', num_features=64,
                                                                 eps=0.0010000000474974513, momentum=0.0)
        self.conv2d_6_bn = self.__batch_normalization(2, 'conv2d_6_bn', num_features=64, eps=0.0010000000474974513,
                                                      momentum=0.0)
        self.cls_2_conv = self.__conv(2, name='cls_2_conv', in_channels=64, out_channels=8, kernel_size=(3, 3),
                                      stride=(1, 1), groups=1, bias=True)
        self.loc_2_conv = self.__conv(2, name='loc_2_conv', in_channels=64, out_channels=16, kernel_size=(3, 3),
                                      stride=(1, 1), groups=1, bias=True)
        self.conv2d_7 = self.__conv(2, name='conv2d_7', in_channels=64, out_channels=64, kernel_size=(3, 3),
                                    stride=(1, 1), groups=1, bias=False)
        self.cls_3_insert_conv2d = self.__conv(2, name='cls_3_insert_conv2d', in_channels=64, out_channels=64,
                                               kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.loc_3_insert_conv2d = self.__conv(2, name='loc_3_insert_conv2d', in_channels=64, out_channels=64,
                                               kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.conv2d_7_bn = self.__batch_normalization(2, 'conv2d_7_bn', num_features=64, eps=0.0010000000474974513,
                                                      momentum=0.0)
        self.cls_3_insert_conv2d_bn = self.__batch_normalization(2, 'cls_3_insert_conv2d_bn', num_features=64,
                                                                 eps=0.0010000000474974513, momentum=0.0)
        self.loc_3_insert_conv2d_bn = self.__batch_normalization(2, 'loc_3_insert_conv2d_bn', num_features=64,
                                                                 eps=0.0010000000474974513, momentum=0.0)
        self.cls_4_insert_conv2d = self.__conv(2, name='cls_4_insert_conv2d', in_channels=64, out_channels=64,
                                               kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.loc_4_insert_conv2d = self.__conv(2, name='loc_4_insert_conv2d', in_channels=64, out_channels=64,
                                               kernel_size=(3, 3), stride=(1, 1), groups=1, bias=False)
        self.cls_3_conv = self.__conv(2, name='cls_3_conv', in_channels=64, out_channels=8, kernel_size=(3, 3),
                                      stride=(1, 1), groups=1, bias=True)
        self.loc_3_conv = self.__conv(2, name='loc_3_conv', in_channels=64, out_channels=16, kernel_size=(3, 3),
                                      stride=(1, 1), groups=1, bias=True)
        self.cls_4_insert_conv2d_bn = self.__batch_normalization(2, 'cls_4_insert_conv2d_bn', num_features=64,
                                                                 eps=0.0010000000474974513, momentum=0.0)
        self.loc_4_insert_conv2d_bn = self.__batch_normalization(2, 'loc_4_insert_conv2d_bn', num_features=64,
                                                                 eps=0.0010000000474974513, momentum=0.0)
        self.cls_4_conv = self.__conv(2, name='cls_4_conv', in_channels=64, out_channels=8, kernel_size=(3, 3),
                                      stride=(1, 1), groups=1, bias=True)
        self.loc_4_conv = self.__conv(2, name='loc_4_conv', in_channels=64, out_channels=16, kernel_size=(3, 3),
                                      stride=(1, 1), groups=1, bias=True)

    def forward(self, x):
        conv2d_0_pad = F.pad(x, (1, 1, 1, 1))
        conv2d_0 = self.conv2d_0(conv2d_0_pad)
        conv2d_0_bn = self.conv2d_0_bn(conv2d_0)
        conv2d_0_activation = F.relu(conv2d_0_bn)
        maxpool2d_0 = F.max_pool2d(conv2d_0_activation, kernel_size=(2, 2), stride=(2, 2), padding=0, ceil_mode=False)
        conv2d_1_pad = F.pad(maxpool2d_0, (1, 1, 1, 1))
        conv2d_1 = self.conv2d_1(conv2d_1_pad)
        conv2d_1_bn = self.conv2d_1_bn(conv2d_1)
        conv2d_1_activation = F.relu(conv2d_1_bn)
        maxpool2d_1 = F.max_pool2d(conv2d_1_activation, kernel_size=(2, 2), stride=(2, 2), padding=0, ceil_mode=False)
        conv2d_2_pad = F.pad(maxpool2d_1, (1, 1, 1, 1))
        conv2d_2 = self.conv2d_2(conv2d_2_pad)
        conv2d_2_bn = self.conv2d_2_bn(conv2d_2)
        conv2d_2_activation = F.relu(conv2d_2_bn)
        maxpool2d_2_pad = F.pad(conv2d_2_activation, (0, 1, 0, 1), value=float('-inf'))
        maxpool2d_2 = F.max_pool2d(maxpool2d_2_pad, kernel_size=(2, 2), stride=(2, 2), padding=0, ceil_mode=False)
        conv2d_3_pad = F.pad(maxpool2d_2, (1, 1, 1, 1))
        conv2d_3 = self.conv2d_3(conv2d_3_pad)
        conv2d_3_bn = self.conv2d_3_bn(conv2d_3)
        conv2d_3_activation = F.relu(conv2d_3_bn)
        maxpool2d_3_pad = F.pad(conv2d_3_activation, (0, 1, 0, 1), value=float('-inf'))
        maxpool2d_3 = F.max_pool2d(maxpool2d_3_pad, kernel_size=(2, 2), stride=(2, 2), padding=0, ceil_mode=False)
        cls_0_insert_conv2d_pad = F.pad(conv2d_3_activation, (1, 1, 1, 1))
        cls_0_insert_conv2d = self.cls_0_insert_conv2d(cls_0_insert_conv2d_pad)
        loc_0_insert_conv2d_pad = F.pad(conv2d_3_activation, (1, 1, 1, 1))
        loc_0_insert_conv2d = self.loc_0_insert_conv2d(loc_0_insert_conv2d_pad)
        conv2d_4_pad = F.pad(maxpool2d_3, (1, 1, 1, 1))
        conv2d_4 = self.conv2d_4(conv2d_4_pad)
        cls_0_insert_conv2d_bn = self.cls_0_insert_conv2d_bn(cls_0_insert_conv2d)
        loc_0_insert_conv2d_bn = self.loc_0_insert_conv2d_bn(loc_0_insert_conv2d)
        conv2d_4_bn = self.conv2d_4_bn(conv2d_4)
        cls_0_insert_conv2d_activation = F.relu(cls_0_insert_conv2d_bn)
        loc_0_insert_conv2d_activation = F.relu(loc_0_insert_conv2d_bn)
        conv2d_4_activation = F.relu(conv2d_4_bn)
        cls_0_conv_pad = F.pad(cls_0_insert_conv2d_activation, (1, 1, 1, 1))
        cls_0_conv = self.cls_0_conv(cls_0_conv_pad)
        loc_0_conv_pad = F.pad(loc_0_insert_conv2d_activation, (1, 1, 1, 1))
        loc_0_conv = self.loc_0_conv(loc_0_conv_pad)
        maxpool2d_4_pad = F.pad(conv2d_4_activation, (0, 1, 0, 1), value=float('-inf'))
        maxpool2d_4 = F.max_pool2d(maxpool2d_4_pad, kernel_size=(2, 2), stride=(2, 2), padding=0, ceil_mode=False)
        cls_1_insert_conv2d_pad = F.pad(conv2d_4_activation, (1, 1, 1, 1))
        cls_1_insert_conv2d = self.cls_1_insert_conv2d(cls_1_insert_conv2d_pad)
        loc_1_insert_conv2d_pad = F.pad(conv2d_4_activation, (1, 1, 1, 1))
        loc_1_insert_conv2d = self.loc_1_insert_conv2d(loc_1_insert_conv2d_pad)
        cls_0_reshape = torch.reshape(input=cls_0_conv.permute(0, 2, 3, 1), shape=(cls_0_conv.size(0), -1, 2))
        loc_0_reshape = torch.reshape(input=loc_0_conv.permute(0, 2, 3, 1), shape=(loc_0_conv.size(0), -1, 4))
        conv2d_5_pad = F.pad(maxpool2d_4, (1, 1, 1, 1))
        conv2d_5 = self.conv2d_5(conv2d_5_pad)
        cls_1_insert_conv2d_bn = self.cls_1_insert_conv2d_bn(cls_1_insert_conv2d)
        loc_1_insert_conv2d_bn = self.loc_1_insert_conv2d_bn(loc_1_insert_conv2d)
        cls_0_activation = F.sigmoid(cls_0_reshape)
        conv2d_5_bn = self.conv2d_5_bn(conv2d_5)
        cls_1_insert_conv2d_activation = F.relu(cls_1_insert_conv2d_bn)
        loc_1_insert_conv2d_activation = F.relu(loc_1_insert_conv2d_bn)
        conv2d_5_activation = F.relu(conv2d_5_bn)
        cls_1_conv_pad = F.pad(cls_1_insert_conv2d_activation, (1, 1, 1, 1))
        cls_1_conv = self.cls_1_conv(cls_1_conv_pad)
        loc_1_conv_pad = F.pad(loc_1_insert_conv2d_activation, (1, 1, 1, 1))
        loc_1_conv = self.loc_1_conv(loc_1_conv_pad)
        maxpool2d_5_pad = F.pad(conv2d_5_activation, (0, 1, 0, 1), value=float('-inf'))
        maxpool2d_5 = F.max_pool2d(maxpool2d_5_pad, kernel_size=(2, 2), stride=(2, 2), padding=0, ceil_mode=False)
        cls_2_insert_conv2d_pad = F.pad(conv2d_5_activation, (1, 1, 1, 1))
        cls_2_insert_conv2d = self.cls_2_insert_conv2d(cls_2_insert_conv2d_pad)
        loc_2_insert_conv2d_pad = F.pad(conv2d_5_activation, (1, 1, 1, 1))
        loc_2_insert_conv2d = self.loc_2_insert_conv2d(loc_2_insert_conv2d_pad)
        cls_1_reshape = torch.reshape(input=cls_1_conv.permute(0, 2, 3, 1), shape=(cls_1_conv.size(0), -1, 2))
        loc_1_reshape = torch.reshape(input=loc_1_conv.permute(0, 2, 3, 1), shape=(loc_1_conv.size(0), -1, 4))
        conv2d_6_pad = F.pad(maxpool2d_5, (1, 1, 1, 1))
        conv2d_6 = self.conv2d_6(conv2d_6_pad)
        cls_2_insert_conv2d_bn = self.cls_2_insert_conv2d_bn(cls_2_insert_conv2d)
        loc_2_insert_conv2d_bn = self.loc_2_insert_conv2d_bn(loc_2_insert_conv2d)
        cls_1_activation = F.sigmoid(cls_1_reshape)
        conv2d_6_bn = self.conv2d_6_bn(conv2d_6)
        cls_2_insert_conv2d_activation = F.relu(cls_2_insert_conv2d_bn)
        loc_2_insert_conv2d_activation = F.relu(loc_2_insert_conv2d_bn)
        conv2d_6_activation = F.relu(conv2d_6_bn)
        cls_2_conv_pad = F.pad(cls_2_insert_conv2d_activation, (1, 1, 1, 1))
        cls_2_conv = self.cls_2_conv(cls_2_conv_pad)
        loc_2_conv_pad = F.pad(loc_2_insert_conv2d_activation, (1, 1, 1, 1))
        loc_2_conv = self.loc_2_conv(loc_2_conv_pad)
        conv2d_7 = self.conv2d_7(conv2d_6_activation)
        cls_3_insert_conv2d_pad = F.pad(conv2d_6_activation, (1, 1, 1, 1))
        cls_3_insert_conv2d = self.cls_3_insert_conv2d(cls_3_insert_conv2d_pad)
        loc_3_insert_conv2d_pad = F.pad(conv2d_6_activation, (1, 1, 1, 1))
        loc_3_insert_conv2d = self.loc_3_insert_conv2d(loc_3_insert_conv2d_pad)
        cls_2_reshape = torch.reshape(input=cls_2_conv.permute(0, 2, 3, 1), shape=(cls_2_conv.size(0), -1, 2))
        loc_2_reshape = torch.reshape(input=loc_2_conv.permute(0, 2, 3, 1), shape=(loc_2_conv.size(0), -1, 4))
        conv2d_7_bn = self.conv2d_7_bn(conv2d_7)
        cls_3_insert_conv2d_bn = self.cls_3_insert_conv2d_bn(cls_3_insert_conv2d)
        loc_3_insert_conv2d_bn = self.loc_3_insert_conv2d_bn(loc_3_insert_conv2d)
        cls_2_activation = F.sigmoid(cls_2_reshape)
        conv2d_7_activation = F.relu(conv2d_7_bn)
        cls_3_insert_conv2d_activation = F.relu(cls_3_insert_conv2d_bn)
        loc_3_insert_conv2d_activation = F.relu(loc_3_insert_conv2d_bn)
        cls_4_insert_conv2d_pad = F.pad(conv2d_7_activation, (1, 1, 1, 1))
        cls_4_insert_conv2d = self.cls_4_insert_conv2d(cls_4_insert_conv2d_pad)
        loc_4_insert_conv2d_pad = F.pad(conv2d_7_activation, (1, 1, 1, 1))
        loc_4_insert_conv2d = self.loc_4_insert_conv2d(loc_4_insert_conv2d_pad)
        cls_3_conv_pad = F.pad(cls_3_insert_conv2d_activation, (1, 1, 1, 1))
        cls_3_conv = self.cls_3_conv(cls_3_conv_pad)
        loc_3_conv_pad = F.pad(loc_3_insert_conv2d_activation, (1, 1, 1, 1))
        loc_3_conv = self.loc_3_conv(loc_3_conv_pad)
        cls_4_insert_conv2d_bn = self.cls_4_insert_conv2d_bn(cls_4_insert_conv2d)
        loc_4_insert_conv2d_bn = self.loc_4_insert_conv2d_bn(loc_4_insert_conv2d)
        cls_3_reshape = torch.reshape(input=cls_3_conv.permute(0, 2, 3, 1), shape=(cls_3_conv.size(0), -1, 2))
        loc_3_reshape = torch.reshape(input=loc_3_conv.permute(0, 2, 3, 1), shape=(loc_3_conv.size(0), -1, 4))
        cls_4_insert_conv2d_activation = F.relu(cls_4_insert_conv2d_bn)
        loc_4_insert_conv2d_activation = F.relu(loc_4_insert_conv2d_bn)
        cls_3_activation = F.sigmoid(cls_3_reshape)
        cls_4_conv_pad = F.pad(cls_4_insert_conv2d_activation, (1, 1, 1, 1))
        cls_4_conv = self.cls_4_conv(cls_4_conv_pad)
        loc_4_conv_pad = F.pad(loc_4_insert_conv2d_activation, (1, 1, 1, 1))
        loc_4_conv = self.loc_4_conv(loc_4_conv_pad)
        cls_4_reshape = torch.reshape(input=cls_4_conv.permute(0, 2, 3, 1), shape=(cls_4_conv.size(0), -1, 2))
        loc_4_reshape = torch.reshape(input=loc_4_conv.permute(0, 2, 3, 1), shape=(loc_4_conv.size(0), -1, 4))
        cls_4_activation = F.sigmoid(cls_4_reshape)
        loc_branch_concat = torch.cat((loc_0_reshape, loc_1_reshape, loc_2_reshape, loc_3_reshape, loc_4_reshape), 1)
        cls_branch_concat = torch.cat(
            (cls_0_activation, cls_1_activation, cls_2_activation, cls_3_activation, cls_4_activation), 1)
        return loc_branch_concat, cls_branch_concat

    @staticmethod
    def __batch_normalization(dim, name, **kwargs):
        if dim == 0 or dim == 1:
            layer = nn.BatchNorm1d(**kwargs)
        elif dim == 2:
            layer = nn.BatchNorm2d(**kwargs)
        elif dim == 3:
            layer = nn.BatchNorm3d(**kwargs)
        else:
            raise NotImplementedError()

        if 'scale' in __weights_dict[name]:
            layer.state_dict()['weight'].copy_(torch.from_numpy(__weights_dict[name]['scale']))
        else:
            layer.weight.data.fill_(1)

        if 'bias' in __weights_dict[name]:
            layer.state_dict()['bias'].copy_(torch.from_numpy(__weights_dict[name]['bias']))
        else:
            layer.bias.data.fill_(0)

        layer.state_dict()['running_mean'].copy_(torch.from_numpy(__weights_dict[name]['mean']))
        layer.state_dict()['running_var'].copy_(torch.from_numpy(__weights_dict[name]['var']))
        return layer

    @staticmethod
    def __conv(dim, name, **kwargs):
        if dim == 1:
            layer = nn.Conv1d(**kwargs)
        elif dim == 2:
            layer = nn.Conv2d(**kwargs)
        elif dim == 3:
            layer = nn.Conv3d(**kwargs)
        else:
            raise NotImplementedError()

        layer.state_dict()['weight'].copy_(torch.from_numpy(__weights_dict[name]['weights']))
        if 'bias' in __weights_dict[name]:
            layer.state_dict()['bias'].copy_(torch.from_numpy(__weights_dict[name]['bias']))
        return layer
