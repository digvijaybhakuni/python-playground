import requests
import cgi




def main():
    files = ["1kGbhAWlrFZygnTCrrxLMVHVeeneVZ1yz",
    "1kGbhAWlrFZygnTCrrxLMVHVeeneVZ1yz", 
    "1Elff9Xu52ry3_oc8_yROm9kHCU9i5uq8", 
    "1j8C5k3S2XhRVP3yGDHh8ADeV6tKxfMKb", 
    "1gwxQcsrtNcPkX8DGuswmkWXHSu-6jN3f", 
    "13QJalYDOOD9L4onhjUh-oYIEAPM08Yq1", 
    "13mgZ78HYBhoVY1-bNph2sRvrYCCylgX2", 
    "1ATiFHXidVtfE2I9lFed_sEntofc6k-M_", 
    "1dMJUq_mMmes12USzV8ZeKWnnUutecpxW", 
    "1kGbhAWlrFZygnTCrrxLMVHVeeneVZ1yz", 
    "1kGbhAWlrFZygnTCrrxLMVHVeeneVZ1yz", 
    "1Elff9Xu52ry3_oc8_yROm9kHCU9i5uq8", 
    "1j8C5k3S2XhRVP3yGDHh8ADeV6tKxfMKb", 
    "1gwxQcsrtNcPkX8DGuswmkWXHSu-6jN3f", 
    "13QJalYDOOD9L4onhjUh-oYIEAPM08Yq1", 
    "13mgZ78HYBhoVY1-bNph2sRvrYCCylgX2", 
    "1ATiFHXidVtfE2I9lFed_sEntofc6k-M_", 
    "1dMJUq_mMmes12USzV8ZeKWnnUutecpxW"]

    for file_id in files:
        download_file(file_id=file_id)


def download_file(file_id):
    # file_id = '1kGbhAWlrFZygnTCrrxLMVHVeeneVZ1yz'

    print("Start downloading " + file_id)

    file_url = "https://drive.google.com/uc?id=" + file_id + "&export=download";

    r = requests.get(file_url, stream = True)

    # header_str = '\r\n'.join('{}: {}'.format(k, v) for k, v in r.headers.items())
    # print(header_str)

    contentDisposition = r.headers.get("Content-Disposition")
    valueContentDisposition, paramscontentDisposition = cgi.parse_header(contentDisposition)

    filename = paramscontentDisposition['filename']
    print("downloading filename " + filename)

    output_file = "D:\\dbx\\gdrive-downloader\\output\\" + filename
    with open(output_file, "wb") as file_output: 
        for chunk in r.iter_content(chunk_size=1024):   
            # writing one chunk at a time to pdf file 
            if chunk: 
                file_output.write(chunk) 


if __name__ == '__main__':
    main()