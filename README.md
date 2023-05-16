# SimpleFast

Welcome to the official repository of **SimpleFast** - an innovative programming language designed to provide simplicity and readability of Python with the performance of C++. It's designed to be user-friendly and approachable for beginners, while also providing the features and performance that advanced users and data scientists need.

## About SimpleFast

SimpleFast is a statically-typed, compiled language that leverages a C++ backend for superior runtime performance. It employs a minimalistic, English-like syntax to make code easy to write and understand.

One of the primary goals of SimpleFast is to make programming more accessible and less daunting for beginners. The syntax is designed to be as intuitive as possible, reducing the cognitive load for new programmers.

At the same time, SimpleFast is designed to be powerful and flexible enough for professional use. The language includes support for advanced features like object-oriented programming, interfaces, and asynchronous I/O.

## Features

- **Simplicity**: SimpleFast's syntax is clean and intuitive, making it easy to learn and use.
- **Performance**: With a C++ backend, SimpleFast offers performance close to that of lower-level languages.
- **Static Typing**: SimpleFast is statically typed which helps catch errors at compile time.
- **Object-Oriented**: SimpleFast supports classes and interfaces, making it suitable for large, complex projects.
- **Asynchronous I/O**: SimpleFast includes built-in support for asynchronous I/O operations, making it great for web and network programming.
- **Machine Learning**: SimpleFast integrates with powerful machine learning libraries, allowing users to build, train, and test complex models with just a few lines of code. Whether you're performing simple linear regression or complex ensemble methods, SimpleFast's intuitive syntax and structure makes the process accessible and efficient.
- **Deep Learning**: With SimpleFast, creating and training deep learning models has never been easier. SimpleFast provides streamlined integration with deep learning libraries, supporting a variety of neural network architectures. From convolutional neural networks (CNNs) for image processing to recurrent neural networks (RNNs) for sequence data, SimpleFast enables you to focus on designing and training your models, not wrestling with syntax.
- **DevOps and AWS Integration**: SimpleFast supports robust integration with AWS and other cloud platforms, making it an excellent tool for DevOps. You can easily set up, automate, and manage your cloud-based workflows, from model training and evaluation to deployment and monitoring. With SimpleFast, you can leverage the full power of AWS services, such as EC2 for compute, S3 for storage, and SageMaker for machine learning, to streamline your ML pipeline. This seamless integration simplifies the process of training models on large datasets in the cloud and deploying trained models for inference at scale.

Some [examples](https://github.com/TheSnowGuru/SimpleFast/blob/main/examples.md) here
- [Hello, World!](https://github.com/TheSnowGuru/SimpleFast/blob/main/examples/hello_world.sfast)
- [All Features](https://github.com/TheSnowGuru/SimpleFast/blob/main/examples/all_features.sfast)
- [AWS Integration](https://github.com/TheSnowGuru/SimpleFast/blob/main/examples/aws_integration.sfast)
- [API Calls](https://github.com/TheSnowGuru/SimpleFast/blob/main/examples/api_calls.sfast)

## Directory Structure:
```
simplefast/
├── src/
│   ├── lexer.py
│   ├── parser.py
│   ├── translator.py
│   ├── compiler.py
│   └── main.py
├── tests/
│   └── test_simplefast.py
├── examples/
│   └── hello_world.sfast
├── LICENSE
└── README.md

```

## File Extension and Compiler

- SimpleFast source files use the `.sfast` file extension.
- The SimpleFast compiler, `sfastc`, compiles `.sfast` files into executable binaries.

## Getting Started

To get started with SimpleFast, check out the documentation in the `docs` directory. You'll find a language reference guide, a tutorial for new users, and several example programs.

## Contributing

We welcome contributions from the community! Whether you're fixing bugs, improving the documentation, or proposing new features, your contributions are greatly appreciated. See the `CONTRIBUTING.md` file for guidelines on how to contribute to SimpleFast.

## License

SimpleFast is open-source software, licensed under the MIT license. See the `LICENSE` file for more details.

Join us in building a language that is not just fast and powerful, but also easy and fun to use! We believe that SimpleFast can be a great tool for learning, teaching, and doing real-world programming, and we're excited to see how you'll use it.
