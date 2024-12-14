import tensorflow as tf

# 모델 정의 (예시)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(8,)),
    tf.keras.layers.Dense(1)
])

# 손실 함수와 옵티마이저 정의
loss_fn = tf.keras.losses.MeanSquaredError()
optimizer = tf.keras.optimizers.Adam()

def train_step(x, y):
    with tf.GradientTape() as tape:
        predictions = model(x)
        loss = loss_fn(y, predictions)
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))
    return loss

# 예시 데이터
x_train = tf.random.normal((32, 8))  # 32개의 샘플, 8개의 특성
y_train = tf.random.normal((32, 1))  # 32개의 타겟 값

# 학습 (epoch 100번)
for epoch in range(100):
    loss = train_step(x_train, y_train)
    tf.print(f"Epoch {epoch+1}, Loss: {loss.numpy()}")