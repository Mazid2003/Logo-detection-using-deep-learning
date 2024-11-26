import tensorflow as tf

# Load the Keras model
model = tf.keras.models.load_model('C:\\Users\\USER\\Desktop\\training\\train\\myapp\\best_model (3).h5')

# List of class names
class_names = ['Adidas', 'Android', 'Apple', 'Ariel', 'Bic','BMW' ,'Burger King', 'Cadbury',
               'Chevrolet', 'Chrome', 'Coca Cola', 'Cowbell', 'Dominos', 'Fila', 'Gillete',
               'Google', 'Goya oil', 'Guinness', 'Heinz', 'Honda', 'Hp', 'Huawei', 'Instagram',
               'Kfc', 'Krisspy Kreme', 'Lays', 'Levis', 'Lg', 'Lipton', 'Mars', 'Marvel',
               'McDonald', 'Mercedes Benz', 'Microsoft', 'MnM', 'Mtn', 'Mtn dew', 'NASA',
               'Nescafe', 'Nestle', 'Nestle milo', 'Netflix', 'Nike', 'Nutella', 'Oral b',
               'Oreo', 'Pay pal', 'Peak milk', 'Pepsi', 'PlayStation', 'Pringles', 'Puma',
               'Reebok', 'Rolex', 'Samsung', 'Sprite', 'Starbucks', 'Tesla', 'Tiktok', 'Twitter',
               'YouTube', 'Zara']
