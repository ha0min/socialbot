# Remotion video

<p align="center">
  <a href="https://github.com/remotion-dev/logo">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github.com/remotion-dev/logo/raw/main/animated-logo-banner-dark.gif">
      <img alt="Animated Remotion Logo" src="https://github.com/remotion-dev/logo/raw/main/animated-logo-banner-light.gif">
    </picture>
  </a>
</p>

Welcome to your TTS Remotion project!

## Get Started

- Create Azure Account
- Create TTS service on Azure
- Create AWS Account
- Setup S3 Bucket with public access
  - Configure bucket policy
    ```json
    {
    	"Version": "2008-10-17",
    	"Statement": [
    		{
    			"Sid": "AllowPublicRead",
    			"Effect": "Allow",
    			"Principal": {
    				"AWS": "*"
    			},
    			"Action": "s3:GetObject",
    			"Resource": "arn:aws:s3:::<YOUR-BUCKET-NAME>/*"
    		}
    	]
    }
    ```
  - Configure bucket CORS
    - Use it only as a template, we recommend you to edit "AllowedOrigins" entering your origin
    ```json
    [
    	{
    		"AllowedHeaders": ["*"],
    		"AllowedMethods": ["HEAD", "GET", "PUT", "POST", "DELETE"],
    		"AllowedOrigins": ["*"],
    		"ExposeHeaders": ["ETag", "x-amz-meta-custom-header"]
    	}
    ]
    ```
- Copy `.env.example` to `.env` entering your secrets
  - ⚠️ Ensure your AWS credentials only allow reading and uploading to a specific S3 bucket `s3:GetObject` and `s3:PutObject` to not compromise your credentials if you deploy your Remotion project
- Use method `textToSpeech` from `src/TextToSpeech/tts.ts` to convert Text to Audio, this method will return file url, you can use it as source of `<Audio />` component

## Example

[![Remotion TTS example](http://img.youtube.com/vi/gbIno38xdhQ/0.jpg)](http://www.youtube.com/watch?v=gbIno38xdhQ 'Remotion TTS example')

## Commands

**Install Dependencies**

```console
npm i
```

**Start Preview**

```console
npm start
```

**Render video**

```console
npm run build
```

See [docs for server-side rendering](https://www.remotion.dev/docs/ssr) here.

**Upgrade Remotion**

```console
npm run upgrade
```

## Docs

Get started with Remotion by reading the [fundamentals page](https://www.remotion.dev/docs/the-fundamentals).

## Issues

Found an issue with Remotion? [File an issue here](https://github.com/JonnyBurger/remotion/issues/new).

## License

Notice that for some entities a company license is needed. Read [the terms here](https://github.com/JonnyBurger/remotion/blob/main/LICENSE.md).
