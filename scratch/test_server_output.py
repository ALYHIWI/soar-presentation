import urllib.request

with urllib.request.urlopen('http://localhost:3000/') as resp:
    print('HTTP Status:', resp.status)
    content = resp.read().decode('utf-8')
    print('Total content length:', len(content))
    print('Has s0:', 'id="s0"' in content)
    print('Has s24:', 'id="s24"' in content)
    print('Has 100 GB:', '100 GB' in content)
    print('Has 22.9%:', '22.9%' in content)
    print('Has 54%:', '54%' in content)
    print('Has 300 µs:', '300 &mu;s' in content or '300 µs' in content)
