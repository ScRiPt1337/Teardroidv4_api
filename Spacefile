# Spacefile Docs: https://go.deta.dev/docs/spacefile/v0
v: 0
icon: static/media/images.png
micros:
  - name: python-app
    src: .
    engine: python3.9
    run: uvicorn main:app
    public_routes:
      - "/client/add"
      - "/command/upload"
      - "/command/complete"
      - "/command/device/*"
      - "/notification/add"

