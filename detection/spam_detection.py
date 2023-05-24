from transformers import pipeline


class SpamDetection():
    _logging  = []

    def __init__(self) -> None:
        '''
        Khởi tạo và nạp mô hình.
        Tải mô hình đã được huấn luyện sẵn và đã được public lên huggingface.
        Nếu mô hình là private, sẽ thực hiện yêu cầu loggin vào huggingface.
        '''
        self.classifier = pipeline("text-classification", model="leeboykt/sms_spam_detection")
        
    def detect(self, text):
        '''
        Interface của class, thực hiện detect tin nhắn sms xem có phải spam hay không
        '''
        data = self.data_processing(text)
        '''
        Thực hiện Inference dữ liệu
        '''
        result  = self.classifier(data)

        '''
        hậu xử lý và trả về kết quả nhận diện
        '''
        return self.post_processing(result)


    def post_processing(self, result):
        
        '''
        Hậu xử lý: Thực hiện các bước hậu xử lý cần thiết với kết quả dự đoán. 
        Các bước hậu xử lý bao gồm: 
        Áp dụng ngưỡng,
        Chuyển đổi điểm dự đoán sang xác suất,
        chuyển đổi sang các nhãn có ý nghĩa hơn.
        Lưu kết quả inference vào trong logging để thực hiện monitor hiệu suất 
        '''
        self.logging = result
        return result[0]
    
    def data_processing(self, data):
        '''
        Xử lý và kiểm tra dữ liệu đã được tải lên
        Data Preprocessing: Implement any necessary data preprocessing steps required before making predictions. This may include scaling, normalization, feature extraction, or data transformation based on the specific requirements of your deep learning model.
        '''
        return data
    
    @property
    def logging(self):
        return self._logging
    
    @logging.getter
    def logging(self):
        return self._logging

    @logging.setter
    def logging(self, result):
        '''
        Thực hiện lưu lại kết quả dự đoán nhằm tính toán hiệu quả mô hình trong thực tế.
        '''
        print(result)
        self._logging.append(result)
    
    def performance(self):
        return None
    