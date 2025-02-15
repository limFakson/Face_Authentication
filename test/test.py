from 

def test_encode_face():
    """
    Test the encode_face function
    """
    face_encoding = encode_face("training/elon_musk/161881.jpg")
    
    sign_in_face(face_encoding[0], encode_face("training/elon_musk/161879.jpg"))
    
    
def sign_in_face(registered_face, unknown_face):
    """
    Sign in the face
    """
    if compare_faces(registered_face, unknown_face):
        print("Face recognized")
    
test_encode_face()