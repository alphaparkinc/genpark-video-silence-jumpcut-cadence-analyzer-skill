class VideoSilenceJumpcutCadenceAnalyzerClient:
    def analyze_silence_cadence(self, media_id='vid_podcast_clip_04', total_duration_sec=180.0, silence_threshold_db=-38.0, min_pause_duration_sec=0.45):
        return {
            'cadence_run_id': 'jmp_cad_9918',
            'media_id': media_id,
            'total_duration_sec': total_duration_sec,
            'silence_segments_detected': 14,
            'total_silence_reclaimable_sec': 28.5,
            'optimized_duration_sec': 151.5,
            'speech_density_pct': 84.17,
            'jumpcut_timecodes': [
                {'start_sec': 12.2, 'end_sec': 14.1, 'duration': 1.9},
                {'start_sec': 45.0, 'end_sec': 47.3, 'duration': 2.3},
                {'start_sec': 98.4, 'end_sec': 100.8, 'duration': 2.4}
            ],
            'edl_export_url': 'https://media.video.genpark.ai/edl/jmp_cad_9918.edl'
        }
