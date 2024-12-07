import { Composition } from "remotion";
import { HelloWorld } from "./HelloWorld";

export const RemotionRoot: React.FC = () => {

  const audioUrl = "https://storage.googleapis.com/newsclip/summary_1684271922.wav";

// 使用 got 创建一个可读流

  return (
    <>
      <Composition
        id="HelloWorld"
        component={HelloWorld}
        durationInFrames={300}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          titleText: "At 10:05, President Joe Biden and top Republican Kevin McCarthy are nearing a deal to avoid a U.S. debt default, with both sides expressing the possibility of reaching an agreement by the end of the week.",
          titleColor: "black",
          audioFileName: audioUrl
        }}
      />
    </>
  );
};
