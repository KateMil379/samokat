# Милейко Екатерина, 10 когорта, финальный проект. Инженер по тестированию плюс.
import sender_stand_request
import data

def test_create_orders_check_status_code():
    response_1 = sender_stand_request.post_new_orders()
    track = str(response_1.json()["track"])
    response_2 = sender_stand_request.get_orders_info(track)
    assert response_2.status_code == 200




