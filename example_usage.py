from client import VideoSilenceJumpcutCadenceAnalyzerClient

def main():
    client = VideoSilenceJumpcutCadenceAnalyzerClient()
    res = client.analyze_silence_cadence()
    print('Silence Jumpcut Analyzer: ' + res['cadence_run_id'] + ' (' + res['media_id'] + ')')
    print('Reclaimed: ' + str(res['total_silence_reclaimable_sec']) + 's | Density: ' + str(res['speech_density_pct']) + '%')
    print('EDL Export URL: ' + res['edl_export_url'])

if __name__ == '__main__':
    main()
