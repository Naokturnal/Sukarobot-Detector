from collections import Counter


def parse_results(results):

    detections = []

    names = []

    for r in results:

        for box in r.boxes:

            cls = int(box.cls)

            conf = float(box.conf)

            label = r.names[cls]

            names.append(label)

            detections.append({

                "class": label,

                "confidence": round(conf, 3),

                "box": box.xyxy.tolist()[0]

            })

    counter = Counter(names)

    return {

        "detections": detections,

        "count": dict(counter),

        "total": len(names)

    }