# FaceAuth - A Simple Face Authentication Library

FaceAuth is a lightweight face authentication library built on top of `face_recognition`. It provides easy-to-use functions for face detection, encoding, and comparison.

## Features
- Encode faces into numerical representations for user
- Compare face encodings to verify identities of user saved
- Supports `HOG` and `CNN` models for face detection

---

## Installation

To use this library run:

```bash
pip install face_auth
```

### Usage

## Encode face ->(known face)
results to be stored in db for future comparison

```python
face_encoding = encode_face("path/to/image.jpg")
# Output: [array([...]), ...]
```
## Compare faces

```python
face_result = compare_faces(known_face, unknown_face)
# Output: bool
```

### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### License
This library is licensed under the MIT License. See the LICENSE file for details.