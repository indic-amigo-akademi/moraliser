from flask import request, jsonify
from chat.api import api_bp


@api_bp.route("/text-validate", methods=["POST"])
def text_chat_validate():
    from chat.utils.text_classifier import TextSpamClassifier, TextProfanityClassifier

    message = request.form.get("message")
    tsc = TextSpamClassifier()
    tpc = TextProfanityClassifier()
    spam_text = "Not a spam!"
    prof_text = "No profane!"
    if tpc.predict_proba(message) != 0:
        prof_text = "Highly profane!"
    if tsc.predict_proba(message) > 0.8:
        spam_text = "Highly spam!"
    elif tsc.predict_proba(message) > 0.6:
        spam_text = "Slightly spam!"
    elif tsc.predict_proba(message) > 0.4:
        spam_text = "Less spam!"
    elif tsc.predict_proba(message) > 0.2:
        spam_text = "I don't think spam!"

    prof_prob = tpc.predict_proba(message)
    if prof_prob > 0.5:
        prof_text = "Profane text!"

    return jsonify(
        {
            "success": True,
            "message": "Chat validation done!",
            "data": {
                "spam_text": f"{spam_text}",
                "prof_text": f"{prof_text}",
            },
        }
    )


@api_bp.route("/link-preview", methods=["POST"])
def get_link_preview():
    url = request.form.get("url")
    from chat.utils.link_preview import LinkPreview
    preview = LinkPreview(url)
    return jsonify(
        {"success": True, "message": "Link preview done!", "data": preview.to_dict()}
    )
