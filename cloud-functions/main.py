from cloudevents.http import CloudEvent
import functions_framework
from google.events.cloud import firestore as firestore_data
from google.cloud import firestore


db = firestore.AsyncClient()


@functions_framework.cloud_event
async def create_data(cloud_event: CloudEvent) -> None:
    """Triggers by a change to a Firestore document.
    Args:
        cloud_event: cloud event with information on the firestore event trigger
    """
    firestore_payload = firestore_data.DocumentEventData()
    firestore_payload._pb.ParseFromString(cloud_event.data)

    print(f"Function triggered by change to: {cloud_event['source']}")
    url_path = firestore_payload.value.name
    print("url_path:::::::::::::::::::::::::::::::::::::::::::::", url_path)
    try:
        await db.collection("data_update").add({
            "change_id": firestore_payload.value.name.split("/")[-1],
            "old": firestore_payload.old_value,
            "new": firestore_payload.value
        })
    except Exception as e:
        print("Something went wrong :", str(e))
