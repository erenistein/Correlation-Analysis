from flask import Flask, render_template, request, send_file
import pandas as pd
import os
import io
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'

# Global değişken
correlation_matrix = None

# Ana sayfa
@app.route('/')
def index():
    return render_template('index.html')


# CSV dosyası yükleme ve korelasyon hesaplama
@app.route('/upload', methods=['POST'])
def upload_file():
    global correlation_matrix  # Global değişken
    if 'file' not in request.files:
        return "Dosya yüklenmedi."
    
    file = request.files['file']

    if file.filename == '':
        return "Geçerli bir dosya seçin."

    if file and file.filename.endswith('.csv'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # CSV'yi pandas ile oku
        try:
            data = pd.read_csv(filepath)
        except Exception as e:
            return f"CSV dosyası okunamadı: {e}"

        # Sadece sayısal sütunları seç
        numeric_data = data.select_dtypes(include=['float64', 'int64'])

        # Eğer sayısal sütun bulunamazsa hata mesajı ver
        if numeric_data.empty:
            return "Veri setinde sayısal sütunlar bulunamadı."

        # NaN olan satırları kaldır
        numeric_data_cleaned = numeric_data.dropna()

        # Eğer tüm satırlar boş veya NaN içeriyorsa uyarı ver
        if numeric_data_cleaned.empty:
            return "Sayısal sütunlar boş veya eksik veriler içeriyor."

        # Korelasyonu hesapla ve global değişkene ata
        correlation_matrix = numeric_data_cleaned.corr()

        # Lineer regresyon modeli eğit
        try:
            # Son sütunu hedef olarak al (y), diğer sütunları X olarak al
            if numeric_data_cleaned.shape[1] < 2:
                return "Yeterli sayıda sütun yok. En az 2 sayısal sütun olmalı."

            X = numeric_data_cleaned.iloc[:, :-1]  # Son sütun hariç tüm sütunlar X
            y = numeric_data_cleaned.iloc[:, -1]   # Son sütun y (hedef)

            # Eğitim ve test veri setlerine ayır
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Modeli oluştur ve eğit
            model = LinearRegression()
            model.fit(X_train, y_train)

            # Test seti üzerinde tahmin yap
            y_pred = model.predict(X_test)

            # Mean Squared Error hesapla
            mse = mean_squared_error(y_test, y_pred)

            # Test verisiyle tahmin sonuçlarını bir DataFrame olarak göster
            predictions_df = pd.DataFrame({'Gerçek Değerler': y_test, 'Tahmin Edilen Değerler': y_pred})

            # Sonuçları HTML template ile döndür
            return render_template(
                'result.html', 
                heatmap_image='/heatmap', 
                mse=mse, 
                tables=[predictions_df.to_html(classes='data table table-bordered', header="true")],
                titles=predictions_df.columns.values
            )

        except Exception as e:
            return f"Model eğitimi sırasında bir hata oluştu: {e}"

    return "Yalnızca CSV dosyaları kabul edilir."


# Korelasyon ısı haritası için bir endpoint
@app.route('/heatmap')
def heatmap():
    global correlation_matrix  # Global değişken
    if correlation_matrix is None:
        return "Korelasyon verisi bulunamadı."

    img = io.BytesIO()
    plt.figure(figsize=(10, 8))  # Isı haritasının boyutunu ayarladık
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')


if __name__ == "__main__":
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
