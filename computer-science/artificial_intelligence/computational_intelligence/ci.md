# Computational Intelligence

A field of artificial intelligence focused on the study of adaptive mechanisms to enable intelligent behavior in complex and changing environments.

`2020, Dec. 17th, Jaroslav Langer`

## Contents <!-- omit in toc -->

- [Abstract](#abstract)
- [Introduction](#introduction)
  - [Introduction](#introduction-1)
  - [Motivation and recent results](#motivation-and-recent-results)
- [Machine Learning](#machine-learning)
  - [History](#history)
  - [Machine learning tasks](#machine-learning-tasks)
  - [Checkers example](#checkers-example)
  - [Machine learning methods](#machine-learning-methods)
  - [Ants AI challenge](#ants-ai-challenge)
- [Evolutionary Algorithms](#evolutionary-algorithms)
- [Neural Networks](#neural-networks)
  - [Overview](#overview)
  - [Perceptron](#perceptron)
  - [Backpropagation algorithm](#backpropagation-algorithm)
  - [Backpropagation algorithm variants](#backpropagation-algorithm-variants)
  - [MLP as universal approximator](#mlp-as-universal-approximator)
  - [Self-organizing Map](#self-organizing-map)
- [Convolutional Networks](#convolutional-networks)
- [Autoencoders](#autoencoders)
- [Text and Graph Embeddings](#text-and-graph-embeddings)
- [Recurrent Neural Networks](#recurrent-neural-networks)
  - [Recurrent Neural Nets](#recurrent-neural-nets)
  - [Attention](#attention)
  - [Differentiable neural computers](#differentiable-neural-computers)
- [Transformers](#transformers)
- [Generative models](#generative-models)
- [Neuroevolution](#neuroevolution)
- [Metalearning](#metalearning)
- [CMAES and Swarm Optimisation](#cmaes-and-swarm-optimisation)

## Abstract

The basis for this document are the lectures form course NI-MVI at FIT CTU, Prague.

## Introduction

- [Computational intelligence vs artificial intelligence](https://ai.stackexchange.com/questions/7446/what-is-the-difference-between-artificial-intelligence-and-computational-intelli#:~:text=In%20the%20modern%20context%2C%20computational,focused%20on%20purely%20deductive%20reasoning.)

### Introduction

#### What is intelligence

#### Evolutionary

#### Genotype phenotype

- fitness function

### Motivation and recent results

#### Significant fields

- self-driving cars
- intelligent assistants
- general artificial intelligence (play game from visual input)

#### Research at Datalab

#### prg.ai

#### ethics

## Machine Learning

### History

- 1940
- 1950
- 1960
- 1970
- 1980
- 1990
- 2000
- 2010
  - GAN
  - Transformers (pros of conv + recu)
- 2020+
  - AutoML in RL

### Machine learning tasks

- regression / prediction
- classification / recomendation
- clustering / 
- problem solving / planing / control 

#### Types learning

- supervised
- unsupervised
- semi-supervised
- Active learning
- transfer learning
- few-shot learning
- meta-learning / continual learning

#### Examples by types

#### Measuring the performance

#### Learning systems

#### Defining learning task

- T - task ()
- P - performance
- E - experience

#### Design learning system

- database, prepare data
- choose what to be learnt - target function
- choose representation of target function
- choose learning algorithm
- supply algorithm with performance metric

### Checkers example

Building the database

- Direct experience
  - set of board with correct move
- indirect experience
  - sequences of game moves and final results

Choose target function

- choseMove(board, legalMoves) -> bestMove
- V(board) -> R (how favorable position) - can be applied for all legalMoves

Choose target function representation

### Machine learning methods

### Ants AI challenge

## Evolutionary Algorithms

## Neural Networks

### Overview

- Introduction to artificial neural networks
- Perceptron, gradient learning
- MLP, Back-propagation of error
- Unsupervised training - SOM

### Perceptron

#### Perceptron training

#### Perceptron gradient learning

#### Deriving gradient of error

#### Cross entropy loss

### Backpropagation algorithm

#### Multilayer perceptron – MLP

#### Chain rule and backprop

#### Training MLP

#### Propagating the error through multiple layers

#### Backprop summary

### Backpropagation algorithm variants

#### Backprop variants

#### Modified transfer functions

#### Backprop with momentum

#### Batch updates and variable learning rate

#### Second order methods

### MLP as universal approximator

### Self-organizing Map

## Convolutional Networks

## Autoencoders

## Text and Graph Embeddings

## Recurrent Neural Networks

- [RNN (Carnegie Mellon University)](http://www.cs.cmu.edu/~mgormley/courses/10601-s18/slides/lecture17-rnn.pdf)

### Recurrent Neural Nets

#### Elman nets

#### Hopfields networks

#### Restricted Boltzmann Machine

#### Supervised training

- Backpropagation through time
- Reservoirs

#### Bidirectional RNN

#### LSTM - Long short-term memory

#### Real-time recurrent learning RTRL

#### Clockwork RNN

#### RNN with stack

#### Neural Turing Machine

### Attention

- In case of autoencoders, the attention mechanism is applied to the decoder part.
- The attention layer (FFN+softmax) define weights to the encoded features so the decoder can easily focus on the more important parts to be decoded right.

### Differentiable neural computers

## Transformers

## Generative models

## Neuroevolution

## Metalearning

## CMAES and Swarm Optimisation
