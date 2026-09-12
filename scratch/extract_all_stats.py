import re

def extract_stats_from_chapter(chap_name, filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print(f"\n=======================================================")
    print(f"STATISTICS AND MEASUREMENTS IN {chap_name}")
    print(f"=======================================================")
    
    # Split sentences roughly
    sentences = re.split(r'(?<=[.!?])\s+', text)
    matched_sentences = []
    
    # regex for numbers with context (exclude pure section numbers like "1.1", "2.3.4")
    num_pattern = re.compile(r'\b(?:\d+(?:\.\d+)?%|\d+(?:,\d+)?\s*(?:gigabytes?|GB|events?|alerts?|incidents?|seconds?|microseconds?|times?|datasets?|hours?|samples?|epochs?)|(?:AUC|recall|precision|score|dwell time|reduction|loss)\b)', re.IGNORECASE)
    
    for s in sentences:
        s_clean = ' '.join(s.split())
        if num_pattern.search(s_clean):
            # check if it's not just a heading or citation year
            matched_sentences.append(s_clean)
            
    print(f"Found {len(matched_sentences)} sentences with statistics/measurements:")
    for idx, s in enumerate(matched_sentences):
        print(f"[{idx+1}] {s}\n")

extract_stats_from_chapter("Chapter 1", "scratch/ch1_full.txt")
extract_stats_from_chapter("Chapter 2", "scratch/ch2_full.txt")
extract_stats_from_chapter("Chapter 3", "scratch/ch3_full.txt")
