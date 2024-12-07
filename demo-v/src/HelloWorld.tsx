import { interpolate, Sequence, useCurrentFrame, useVideoConfig } from "remotion";
import { Title } from "./News/Title";

export const HelloWorld: React.FC<{
  titleText: string;
  titleColor: string;
  audioFileName: string;
}> = ({ titleText, titleColor, audioFileName }) => {
  const frame = useCurrentFrame();
  const videoConfig = useVideoConfig();

  const opacity = interpolate(
    frame,
    [videoConfig.durationInFrames - 25, videoConfig.durationInFrames - 15],
    [1, 0],
    {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp"
    }
  );
  const transitionStart = 25;

  return (
    <div style={{ flex: 1, backgroundColor: "white" }}>
      <div style={{ opacity }}>
        <Sequence from={transitionStart + 10}>
          <Title titleText={titleText}
								 titleColor={titleColor}
								 audioFileName={audioFileName} />
        </Sequence>
      </div>
    </div>
  );
};
